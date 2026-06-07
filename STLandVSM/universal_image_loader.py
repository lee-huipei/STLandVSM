import os
import numpy as np
import torch
import folder_paths

# 尝试 OIIO（专业图像加载）
try:
    import OpenImageIO as oiio
    OIIO_AVAILABLE = True
except ImportError:
    OIIO_AVAILABLE = False

# PIL 作为后备（支持几乎所有格式）
from PIL import Image

SUPPORTED_FORMATS = (".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff", ".webp", ".exr", ".gif", ".ico", ".dds", ".psd", ".hdr", ".sgi", ".tga")

class UniversalImageLoader:
    """万能图片加载节点 - 使用 OIIO 加载，保留完整位深"""
    
    @classmethod
    def INPUT_TYPES(cls):
        input_dir = folder_paths.get_input_directory()
        output_dir = folder_paths.get_output_directory()
        files = []
        seen = set()
        for directory in [input_dir, output_dir]:
            if os.path.exists(directory):
                for f in sorted(os.listdir(directory)):
                    fp = os.path.join(directory, f)
                    if os.path.isfile(fp) and f not in seen:
                        ext = os.path.splitext(f)[1].lower()
                        if ext in SUPPORTED_FORMATS:
                            files.append(f)
                            seen.add(f)
        return {
            "required": {
                "image": (sorted(files), {"image_upload": True}),
            }
        }
    
    CATEGORY = "STLandVSM"
    RETURN_TYPES = ("IMAGE", "MASK")
    FUNCTION = "load_image"
    
    def load_image(self, image, filepath=""):
        # Try input dir first, then output dir
        image_path = folder_paths.get_annotated_filepath(image)
        if not os.path.exists(image_path):
            image_path = os.path.join(folder_paths.get_output_directory(), image)
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"找不到文件: {image}（请将文件放到 ComfyUI/input 或 output 目录）")
        
        # 尝试 OIIO 加载（保留完整精度）
        img_array = None
        if OIIO_AVAILABLE:
            img_array = self._load_with_oiio(image_path)
        
        # OIIO 失败时用 PIL
        if img_array is None:
            img_array = self._load_with_pil(image_path)
        
        if img_array is None:
            raise RuntimeError(f"无法加载图像: {image_path}")
        
        # 输出为标准 IMAGE 张量
        img_tensor = torch.from_numpy(img_array).unsqueeze(0)
        
        # 生成空 MASK
        h, w = img_array.shape[:2]
        mask = torch.zeros((64, 64), dtype=torch.float32)
        
        return (img_tensor, mask)
    
    def _load_with_oiio(self, path):
        """使用 OpenImageIO 加载，保留完整浮点精度"""
        try:
            buf = oiio.ImageBuf(path)
            spec = buf.spec()
            w, h = spec.width, spec.height
            channels = spec.nchannels
            
            roi = oiio.ROI(0, w, 0, h, 0, 1, 0, channels)
            pixels = buf.get_pixels(roi=roi)
            
            if pixels is None:
                return None
            
            pixels = np.array(pixels, dtype=np.float32)
            
            # OIIO 返回 (H, W, C) 格式
            if len(pixels.shape) == 2:
                pixels = pixels.reshape(h, w, 1)
            
            # OIIO 读取的 EXR 已经在 0-1 范围，无需归一化
            # 但对 PNG/JPG/TIF 等整数格式，需要归一化
            ext = os.path.splitext(path)[1].lower()
            if ext not in ('.exr', '.hdr'):
                if pixels.max() > 1.0:
                    if pixels.max() > 255:
                        pixels = pixels / 65535.0
                    else:
                        pixels = pixels / 255.0
            
            print(f"[UniversalLoader] 像素范围: [{pixels.min():.6f}, {pixels.max():.6f}]")
            
            # 单通道扩展为 3 通道
            if pixels.shape[2] == 1:
                pixels = np.repeat(pixels, 3, axis=2)
            elif pixels.shape[2] > 3:
                pixels = pixels[:,:,:3]
            
            print(f"[UniversalLoader] OIIO读取: {w}x{h}x{channels}, 范围[{pixels.min():.4f}, {pixels.max():.4f}]")
            return pixels
            
        except Exception as e:
            print(f"[UniversalLoader] OIIO加载失败，回退到PIL: {e}")
            return None
    
    def _load_with_pil(self, path):
        """PIL 后备加载"""
        try:
            img = Image.open(path)
            mode = img.mode
            
            # 处理高位深图像（I;16, I 等）
            if mode in ('I;16', 'I;16L', 'I;16B', 'I'):
                # 转 32 位浮点再归一化
                arr = np.array(img, dtype=np.float32)
                if arr.max() > 1.0:
                    if arr.max() > 65535:
                        arr = arr / 16777215.0
                    elif arr.max() > 255:
                        arr = arr / 65535.0
                    else:
                        arr = arr / 255.0
                
                if len(arr.shape) == 2:
                    arr = arr.reshape(arr.shape[0], arr.shape[1], 1)
                
                if arr.shape[2] == 1:
                    arr = np.repeat(arr, 3, axis=2)
                
                print(f"[UniversalLoader] PIL高精度: {img.size}, 范围[{arr.min():.4f}, {arr.max():.4f}]")
                return arr
            
            # 普通 8 位图像
            img = img.convert("RGB")
            arr = np.array(img, dtype=np.float32) / 255.0
            print(f"[UniversalLoader] PIL读取: {img.size}, 范围[{arr.min():.4f}, {arr.max():.4f}]")
            return arr
            
        except Exception as e:
            print(f"[UniversalLoader] PIL加载失败: {e}")
            return None

    @classmethod
    def IS_CHANGED(cls, image):
        import hashlib
        # Try input dir first, then output dir
        image_path = folder_paths.get_annotated_filepath(image)
        if not os.path.exists(image_path):
            image_path = os.path.join(folder_paths.get_output_directory(), image)
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"找不到文件: {image}（请将文件放到 ComfyUI/input 或 output 目录）")
        with open(image_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()

    @classmethod
    def VALIDATE_INPUTS(cls, image):
        if not folder_paths.exists_annotated_filepath(image):
            return f"文件不存在: {image}"
        return True










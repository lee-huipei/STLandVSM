import os
import time
import folder_paths


class GLBPreview:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "glb_path": ("STRING", {"forceInput": True}),
                "显示模式": (["实体", "彩色地形"], {"default": "彩色地形"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("preview_filename",)
    OUTPUT_NODE = True
    FUNCTION = "preview"
    CATEGORY = "3D/预览"

    def preview(self, glb_path, 显示模式="彩色地形"):
        if 显示模式 not in ("实体", "彩色地形"):
            显示模式 = "彩色地形"
        if glb_path and os.path.exists(glb_path):
            basename = os.path.basename(glb_path)
            return (basename,)
        return ("",)

    @classmethod
    def IS_CHANGED(cls, glb_path, 显示模式="彩色地形"):
        return time.time()


NODE_CLASS_MAPPINGS = {
    "GLBPreview": GLBPreview,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GLBPreview": "GLB预览",
}

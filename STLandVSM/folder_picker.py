import os
import json
import server
from aiohttp import web
import folder_paths

try:
    import tkinter as tk
    from tkinter import filedialog
    HAS_TK = True
except ImportError:
    HAS_TK = False
    print("[文件夹选择器] tkinter 未安装")

CONFIG_FILE = os.path.join(os.path.dirname(__file__), 'folder_path.json')

def get_saved_path():
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                path = data.get('path', '')
                if path and os.path.exists(path):
                    return path
    except Exception as e:
        print(f"[文件夹选择器] 读取失败: {e}")
    return ""

def save_path(path):
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump({'path': path}, f, ensure_ascii=False)
    except Exception as e:
        print(f"[文件夹选择器] 保存失败: {e}")


class FolderPicker:
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "hidden": {"prompt": "PROMPT"}
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("文件夹路径",)
    OUTPUT_NODE = True
    FUNCTION = "get_path"
    CATEGORY = "3D/工具"
    
    def get_path(self, prompt):
        saved = get_saved_path()
        if saved:
            return (saved,)
        return (folder_paths.get_output_directory(),)
    
    @staticmethod
    def select_folder():
        current = get_saved_path() or folder_paths.get_output_directory()
        if not HAS_TK:
            return current
        try:
            root = tk.Tk()
            root.withdraw()
            root.attributes('-topmost', True)
            folder = filedialog.askdirectory(initialdir=current, title="选择输出文件夹")
            root.destroy()
            if folder and os.path.exists(folder):
                save_path(folder)
                return folder
        except Exception as e:
            print(f"[文件夹选择器] 选择失败: {e}")
        return current
    
    @staticmethod
    def reset():
        save_path("")
        return folder_paths.get_output_directory()


@server.PromptServer.instance.routes.get("/folder-picker/select")
async def select_route(request):
    folder = FolderPicker.select_folder()
    return web.json_response({'selected_folder': folder})

@server.PromptServer.instance.routes.get("/folder-picker/get")
async def get_route(request):
    saved = get_saved_path()
    default = folder_paths.get_output_directory()
    return web.json_response({
        'selected_folder': saved,
        'default_path': default,
        'has_tk': HAS_TK
    })

@server.PromptServer.instance.routes.get("/folder-picker/reset")
async def reset_route(request):
    default = FolderPicker.reset()
    return web.json_response({'success': True, 'default_path': default})


NODE_CLASS_MAPPINGS = {"FolderPicker": FolderPicker}
NODE_DISPLAY_NAME_MAPPINGS = {"FolderPicker": "📁 文件夹选择器"}
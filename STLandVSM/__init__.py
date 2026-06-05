import os, sys, shutil, folder_paths

_my_dir = os.path.dirname(os.path.abspath(__file__))

_PKG = __name__  # ComfyUI may register module under different name

def _load_core(name):
    import importlib.machinery, importlib.util
    # Try .pyc first (encrypted mode)
    pyc_path = os.path.join(_my_dir, name + ".cpython-313.pyc")
    if not os.path.exists(pyc_path):
        pyc_path = os.path.join(_my_dir, name + ".pyc")
    if os.path.exists(pyc_path):
        module_name = _PKG + "." + name
        loader = importlib.machinery.SourcelessFileLoader(module_name, pyc_path)
        spec = importlib.util.spec_from_loader(module_name, loader, origin=pyc_path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = mod
        loader.exec_module(mod)
        return mod
    # Fallback: try standard import (for .py source)
    try:
        import importlib as _il
        mod = _il.import_module("." + name, package=_PKG)
        sys.modules[_PKG + "." + name] = mod
        return mod
    except:
        return None

_license_mod = _load_core("_license")
_exr_mod = _load_core("exr_handler")
_stl_mod = _load_core("img_to_stl")
_vsm_mod = _load_core("img_to_vsm")
_main_mod = _load_core("stl_vsm_converter")

if _license_mod:
    _valid, _msg = _license_mod.verify_license()
    if _valid:
        print("[STLandVSM] License OK: " + str(_msg))
    else:
        print("[STLandVSM] WARNING: " + str(_msg))
        print("[STLandVSM] Contact for license")

import re as _re
def _get_status_suffix():
    global _valid, _msg
    if not _valid:
        m = str(_msg).lower() if _msg else ""
        if "trial expired" in m or "expired" in m:
            return " ✗过期"
        if "trial record" in m or "abnormal" in m:
            return " ✗异常"
        return " ✗未激活"
    m = str(_msg).lower()
    if "permanent" in m:
        return " ★永久"
    if "trial" in m:
        if "started" in m:
            return " ⏳试用7天"
        mt = _re.search(r"remaining\s+(\d+)", m)
        if mt:
            return " ⏳试用" + mt.group(1) + "天"
        return " ⏳试用"
    if "remaining" in m:
        mt = _re.search(r"remaining\s+(\d+)", m)
        if mt:
            return " ⏳" + mt.group(1) + "天"
        return " ⏳限时"
    return ""

if _license_mod:
    _status_suffix = _get_status_suffix()
    if _status_suffix:
        print("[STLandVSM] Status: [" + _status_suffix + "]")
else:
    _status_suffix = ""

os.makedirs(os.path.join(folder_paths.get_output_directory(), "STL"), exist_ok=True)
os.makedirs(os.path.join(folder_paths.get_output_directory(), "VSM"), exist_ok=True)

_preview_dir = os.path.join(folder_paths.get_output_directory(), "glb_preview")
os.makedirs(_preview_dir, exist_ok=True)
_brand_path = os.path.join(_my_dir, "assets", "branding.glb")
if os.path.exists(_brand_path):
    _dest = os.path.join(_preview_dir, "branding.glb")
    if not os.path.exists(_dest) or os.path.getsize(_dest) != os.path.getsize(_brand_path):
        shutil.copy2(_brand_path, _dest)
        print("[STLandVSM] Branding model copied: " + str(_dest))

from .safe_preview_bridge import Safe3DPreviewBridge
from .folder_picker import FolderPicker
from .bool_switch import BoolSwitch
from .format_selector import FormatSelector
from .glb_preview import NODE_CLASS_MAPPINGS as GLB_MAPPINGS
from .glb_preview import NODE_DISPLAY_NAME_MAPPINGS as GLB_DISPLAY

_base_name = "STL & VSM Conv" + _status_suffix

NODE_CLASS_MAPPINGS = {
    "STLVSMConverter": _main_mod.STLVSMConverter if _main_mod else None,
    "Safe3DPreviewBridge": Safe3DPreviewBridge,
    "FolderPicker": FolderPicker,
    "BoolSwitch": BoolSwitch,
    "FormatSelector": FormatSelector,
    **GLB_MAPPINGS,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "STLVSMConverter": _base_name,
    "Safe3DPreviewBridge": "安全3D预览桥接",
    "FolderPicker": "📁 文件夹选择器",
    "BoolSwitch": "🔘 布尔开关",
    "FormatSelector": "📋 格式选择器",
    **GLB_DISPLAY,
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
WEB_DIRECTORY = "./web"

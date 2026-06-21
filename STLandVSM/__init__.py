# coding: utf-8

import os,sys,hashlib,base64,shutil,folder_paths
_j=os.path.dirname(os.path.abspath(__file__))
_l=__name__
_k=hashlib.sha256(b"GMHD_STLandVSM_2026_SIGN").digest()

def _f(n):
 try:
  p=os.path.join(_j,n+".enc")
  with open(p,"r",encoding="ascii")as h:c=h.read()
  d=base64.b64decode(c);r=bytearray()
  for i,b in enumerate(d):r.append(b^_k[i%len(_k)])
  mn=_l+"."+n;m=type(n,(),{})()
  m.__dict__["__name__"]=mn;m.__dict__["__file__"]=p
  m.__dict__["__spec__"]=None;m.__dict__["__builtins__"]=__builtins__
  sys.modules[mn]=m;exec(compile(bytes(r),p,"exec"),m.__dict__);return m
 except Exception as e:print("[STLandVSM]load "+n+".enc failed:"+str(e)[:80]);return None

_m__license=_f("_license")
_m_exr_handler=_f("exr_handler")
_m_format_selector=_f("format_selector")
_m_glb_preview=_f("glb_preview")
_m_img_to_stl=_f("img_to_stl")
_m_img_to_vsm=_f("img_to_vsm")
_m_safe_preview_bridge=_f("safe_preview_bridge")
_m_stl_vsm_converter=_f("stl_vsm_converter")
_m_universal_image_loader=_f("universal_image_loader")

from.bool_switch import*;from.folder_picker import*
_lic_mod=_m__license
if _lic_mod:
 try:_lic_valid,_lic_msg=_lic_mod.verify_license()
 except:_lic_valid=False;_lic_msg="verify error"
 if _lic_valid:print("[STLandVSM]License OK:"+str(_lic_msg))
 else:print("[STLandVSM]WARNING:"+str(_lic_msg))
else:_lic_valid=False;_lic_msg=""
import re as _re
def _s():
 global _lic_valid,_lic_msg
 if not _lic_valid:return" X"
 m=str(_lic_msg).lower()
 if"permanent"in m:return" P"
 if"trial"in m:
  if"started"in m:return" T7d"
  mt=_re.search(r"remaining\s+(\d+)",m)
  if mt:return" T"+mt.group(1)+"d";return" T"
 if"activated"in m:
   mt=_re.search(r"(\d+) days",m)
   if mt:return" "+mt.group(1)+"d";return" A"
 if"remaining"in m:
  mt=_re.search(r"remaining\s+(\d+)",m)
  if mt:return" "+mt.group(1)+"d";return" L"
 return""
_ss=_s()if _lic_mod else""
if _ss:print("[STLandVSM]Status:["+_ss+"]")
_=os
_.makedirs(_.path.join(folder_paths.get_output_directory(),"STL"),exist_ok=True)
_.makedirs(_.path.join(folder_paths.get_output_directory(),"VSM"),exist_ok=True)
_pd=_.path.join(folder_paths.get_output_directory(),"glb_preview")
_.makedirs(_pd,exist_ok=True)
_bp=_.path.join(_.path.dirname(_.path.abspath(__file__)),"assets","branding.glb")
if _.path.exists(_bp):
 _bd=_.path.join(_pd,"branding.glb")
 if not _.path.exists(_bd)or _.path.getsize(_bd)!=_.path.getsize(_bp):shutil.copy2(_bp,_bd)
_SB=getattr(_m_safe_preview_bridge,"Safe3DPreviewBridge",None)if _m_safe_preview_bridge else None
_FS=getattr(_m_format_selector,"FormatSelector",None)if _m_format_selector else None
_UL=getattr(_m_universal_image_loader,"UniversalImageLoader",None)if _m_universal_image_loader else None
_GM=getattr(_m_glb_preview,"NODE_CLASS_MAPPINGS",{})if _m_glb_preview else{}
_GD=getattr(_m_glb_preview,"NODE_DISPLAY_NAME_MAPPINGS",{})if _m_glb_preview else{}
_conv=getattr(_m_stl_vsm_converter,"STLVSMConverter",None)if _m_stl_vsm_converter else None
_BS,_FP=BoolSwitch,FolderPicker
_base="STL & VSM Conv"+_ss
NODE_CLASS_MAPPINGS={"STLVSMConverter":_conv,"Safe3DPreviewBridge":_SB,"FolderPicker":_FP,"BoolSwitch":_BS,"FormatSelector":_FS,"UniversalImageLoader":_UL,**_GM}
NODE_DISPLAY_NAME_MAPPINGS={"STLVSMConverter":_base,"Safe3DPreviewBridge":"安全3D预览桥接","FolderPicker":"📁 文件夹选择器","BoolSwitch":"🔘 布尔开关","FormatSelector":"📋 图像格式选择器","UniversalImageLoader":"加载图像 (高精度)",**_GD}
__all__=["NODE_CLASS_MAPPINGS","NODE_DISPLAY_NAME_MAPPINGS"];WEB_DIRECTORY="./web"
import os
import folder_paths
import time


class Safe3DPreviewBridge:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model_path": ("STRING", {"forceInput": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("safe_model_path",)
    FUNCTION = "check_path"
    CATEGORY = "3D/桥接"
    OUTPUT_NODE = True

    def check_path(self, model_path):
        print(f"[桥接节点] 收到路径: {model_path}")

        # 品牌模型路径
        current_dir = os.path.dirname(os.path.abspath(__file__))
        branding_path = os.path.join(current_dir, "assets", "branding.glb")

        # 优先：用户已生成的模型存在 → 展示用户模型
        if model_path and os.path.exists(model_path):
            print(f"[桥接节点] 用户模型存在，返回: {model_path}")
            return (model_path,)

        # 降级：展示品牌模型（空载/首次加载时）
        if os.path.exists(branding_path):
            print(f"[桥接节点] 无用户模型，返回品牌: {branding_path}")
            return (branding_path,)

        print(f"[桥接节点] 无可用模型，返回空")
        return ("",)

    @classmethod
    def IS_CHANGED(cls, model_path):
        return time.time()


NODE_CLASS_MAPPINGS = {
    "Safe3DPreviewBridge": Safe3DPreviewBridge,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Safe3DPreviewBridge": "安全3D预览桥接",
}

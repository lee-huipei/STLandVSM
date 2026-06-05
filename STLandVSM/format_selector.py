class FormatSelector:
    """格式选择器 - 输出格式名称供 STLVSMConverter 使用"""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "格式": (["PNG", "EXR", "TIF", "BMP", "无"], {"default": "EXR"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("格式",)
    FUNCTION = "select"
    CATEGORY = "3D/工具"

    def select(self, 格式="EXR"):
        return (格式,)


NODE_CLASS_MAPPINGS = {
    "FormatSelector": FormatSelector,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FormatSelector": "📋 格式选择器",
}

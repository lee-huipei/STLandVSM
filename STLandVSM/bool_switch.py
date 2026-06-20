"""
布尔开关节点 - 通用版
"""

import server
from aiohttp import web


class BoolSwitch:
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "hidden": {
                "prompt": "PROMPT",
                "unique_id": "UNIQUE_ID",  # 使用 ComfyUI 给的唯一 ID
            }
        }
    
    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("布尔值",)
    OUTPUT_NODE = True
    FUNCTION = "get_value"
    CATEGORY = "3D/工具"
    
    def get_value(self, prompt, unique_id):
        state = bool_states.get(unique_id, True)
        return (state,)


# 存储状态（用 unique_id 作为 key）
bool_states = {}


@server.PromptServer.instance.routes.get("/bool-switch/toggle")
async def toggle_route(request):
    node_id = request.rel_url.query.get('id', '')
    if node_id:
        current = bool_states.get(node_id, True)
        bool_states[node_id] = not current
        return web.json_response({'state': bool_states[node_id]})
    return web.json_response({'state': True})


@server.PromptServer.instance.routes.get("/bool-switch/get")
async def get_route(request):
    node_id = request.rel_url.query.get('id', '')
    state = bool_states.get(node_id, True)
    return web.json_response({'state': state})


NODE_CLASS_MAPPINGS = {"BoolSwitch": BoolSwitch}
NODE_DISPLAY_NAME_MAPPINGS = {"BoolSwitch": "🔘 布尔开关"}
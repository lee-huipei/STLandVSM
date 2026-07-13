"""
布尔开关节点 - 通用版
"""
import os
import json
import server
from aiohttp import web


# 状态文件路径（节点目录下的 state.json，统一存储所有持久化状态）
_STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "state.json")

# 存储状态（用 unique_id 作为 key）
bool_states = {}


def _load_states():
    """启动时从 state.json 恢复所有持久化状态"""
    global bool_states
    try:
        if os.path.exists(_STATE_FILE):
            with open(_STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            bool_states = data.get("bool_switches", {})
            print(f"[BoolSwitch] 加载了 {len(bool_states)} 个状态: {json.dumps(bool_states)}")
        else:
            bool_states = {}
            print("[BoolSwitch] state.json 不存在，使用空状态")
    except Exception as e:
        print(f"[BoolSwitch] 加载状态失败: {e}")
        bool_states = {}


def _save_states():
    """保存所有持久化状态到 state.json（不覆盖其他模块的数据）"""
    try:
        all_data = {}
        if os.path.exists(_STATE_FILE):
            with open(_STATE_FILE, "r", encoding="utf-8") as f:
                all_data = json.load(f)
        all_data["bool_switches"] = bool_states
        with open(_STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
        print(f"[BoolSwitch] 保存了 {len(bool_states)} 个状态")
    except Exception as e:
        print(f"[BoolSwitch] 保存状态失败: {e}")


# 模块加载时自动恢复状态
_load_states()


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
        # 记忆中有就按记忆，没有就默认关
        # 注意：unique_id 可能是整数，而 JSON 存储的 key 是字符串，统一转 str
        uid = str(unique_id)
        state = bool_states.get(uid, False)
        print(f"[BoolSwitch] get_value: unique_id={unique_id}({type(unique_id).__name__}) str={uid} → {state}")
        return (state,)


@server.PromptServer.instance.routes.get("/bool-switch/toggle")
async def toggle_route(request):
    node_id = request.rel_url.query.get('id', '')
    if node_id:
        current = bool_states.get(node_id, False)
        bool_states[node_id] = not current
        _save_states()  # 切换后立即保存
        print(f"[BoolSwitch] toggle: id={node_id} → {bool_states[node_id]}")
        return web.json_response({'state': bool_states[node_id]})
    return web.json_response({'state': False})


@server.PromptServer.instance.routes.get("/bool-switch/get")
async def get_route(request):
    node_id = request.rel_url.query.get('id', '')
    state = bool_states.get(node_id, False)
    print(f"[BoolSwitch] get: id={node_id}(type={type(node_id).__name__}) → {state} (字典keys例: {list(bool_states.keys())[:3]})")
    return web.json_response({'state': state})


# 调试用：查看当前所有状态
@server.PromptServer.instance.routes.get("/bool-switch/debug")
async def debug_route(request):
    return web.json_response({
        'state_file': _STATE_FILE,
        'file_exists': os.path.exists(_STATE_FILE),
        'states': bool_states,
        'state_count': len(bool_states),
    })


NODE_CLASS_MAPPINGS = {"BoolSwitch": BoolSwitch}
NODE_DISPLAY_NAME_MAPPINGS = {"BoolSwitch": "🔘 布尔开关"}

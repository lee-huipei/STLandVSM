import { api } from "../../../scripts/api.js";
import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "STLandVSM.BoolSwitch",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name !== "BoolSwitch") return;

        const onNodeCreated = nodeType.prototype.onNodeCreated;
        nodeType.prototype.onNodeCreated = async function () {
            const result = onNodeCreated?.apply(this, arguments);
            const node = this;

            let currentState = true;

            const updateState = async () => {
                try {
                    const res = await api.fetchApi(`/bool-switch/toggle?id=${node.id}`);
                    const data = await res.json();
                    currentState = data.state;
                    
                    // 更新按钮文字
                    btn.name = currentState ? "🟢 开启" : "🔴 关闭";
                    btn.label = currentState ? "🟢 开启" : "🔴 关闭";
                    
                    // 更新输出
                    node.setOutputData(0, currentState);
                    app.graph.setDirtyCanvas(true);
                } catch (error) {
                    console.error("切换失败:", error);
                }
            };

            // 创建按钮
            const btn = node.addWidget("button", "🟢 开启", null, async () => {
                await updateState();
            });

            // 加载当前状态
            try {
                const res = await api.fetchApi(`/bool-switch/get?id=${node.id}`);
                const data = await res.json();
                currentState = data.state;
                btn.name = currentState ? "🟢 开启" : "🔴 关闭";
                btn.label = currentState ? "🟢 开启" : "🔴 关闭";
                node.setOutputData(0, currentState);
            } catch (error) {
                console.error("加载状态失败:", error);
            }

            return result;
        };
    }
});
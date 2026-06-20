import { api } from "../../../scripts/api.js";
import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "STLandVSM.FolderPicker",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name !== "FolderPicker") return;

        const onNodeCreated = nodeType.prototype.onNodeCreated;
        nodeType.prototype.onNodeCreated = async function () {
            const result = onNodeCreated?.apply(this, arguments);
            const node = this;

            const updateOutput = (path) => {
                node.setOutputData(0, path);
                node.onResize?.(node.size);
                app.graph.setDirtyCanvas(true);
            };

            const pathWidget = node.addWidget("text", "文件夹路径", "", updateOutput);

            node.addWidget("button", "📁 选择文件夹", null, async () => {
                try {
                    const res = await api.fetchApi("/folder-picker/select");
                    const data = await res.json();
                    if (data.selected_folder) {
                        pathWidget.value = data.selected_folder;
                        updateOutput(data.selected_folder);
                    }
                } catch (error) {
                    console.error("选择失败:", error);
                }
            });

            node.addWidget("button", "↺ 恢复系统默认", null, async () => {
                try {
                    const res = await api.fetchApi("/folder-picker/reset");
                    const data = await res.json();
                    if (data.success) {
                        pathWidget.value = data.default_path;
                        updateOutput(data.default_path);
                    }
                } catch (error) {
                    console.error("恢复失败:", error);
                }
            });

            try {
                const res = await api.fetchApi("/folder-picker/get");
                const data = await res.json();
                const path = data.selected_folder || data.default_path;
                pathWidget.value = path;
                updateOutput(path);
            } catch (error) {
                console.error("加载失败:", error);
            }

            return result;
        };
    }
});
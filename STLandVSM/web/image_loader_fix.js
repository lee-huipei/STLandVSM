import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "STLandVSM.ImageLoaderFix",
    async beforeRegisterNodeDef(nodeType, nodeData) {
        if (nodeData.name !== "UniversalImageLoaderFixed") return;

        const origOnNodeCreated = nodeType.prototype.onNodeCreated;
        nodeType.prototype.onNodeCreated = function () {
            const result = origOnNodeCreated?.apply(this, arguments);

            const imageWidget = this.widgets?.find(w => w.name === "image");
            if (!imageWidget) return result;

            // 保存原始回调
            const origCallback = imageWidget.callback;

            // 在节点上添加一个自定义上传按钮
            const uploadBtn = document.createElement("button");
            uploadBtn.textContent = "📁 选择文件";
            uploadBtn.style.cssText = "margin:2px 0;padding:3px 8px;cursor:pointer;background:#333;color:#fff;border:1px solid #555;border-radius:3px;width:100%";

            uploadBtn.onclick = async () => {
                // 创建隐藏的文件输入
                const input = document.createElement("input");
                input.type = "file";
                input.accept = ".png,.jpg,.jpeg,.bmp,.tif,.tiff,.webp,.exr,.hdr,.gif";

                input.onchange = async () => {
                    const file = input.files[0];
                    if (!file) return;

                    uploadBtn.textContent = "⏳ 上传中...";
                    uploadBtn.disabled = true;

                    try {
                        // 上传文件到 ComfyUI
                        const formData = new FormData();
                        formData.append("image", file);
                        formData.append("type", "input");
                        formData.append("overwrite", "true");

                        const resp = await fetch("/upload/image", {
                            method: "POST",
                            body: formData
                        });

                        if (!resp.ok) {
                            uploadBtn.textContent = "❌ 上传失败";
                            setTimeout(() => { uploadBtn.textContent = "📁 选择文件"; uploadBtn.disabled = false; }, 2000);
                            return;
                        }

                        const result = await resp.json();
                        const filename = result.name;

                        // 更新下拉列表 - 添加新文件
                        if (!imageWidget.options.values.includes(filename)) {
                            imageWidget.options.values.push(filename);
                        }

                        // 选中新上传的文件
                        imageWidget.value = filename;
                        if (origCallback) origCallback(filename);

                        uploadBtn.textContent = "✅ " + filename;
                        setTimeout(() => { uploadBtn.textContent = "📁 选择文件"; uploadBtn.disabled = false; }, 1500);

                    } catch (err) {
                        uploadBtn.textContent = "❌ 出错";
                        setTimeout(() => { uploadBtn.textContent = "📁 选择文件"; uploadBtn.disabled = false; }, 2000);
                    }
                };
                input.click();
            };

            // 将按钮添加到节点
            const el = this.el?.querySelector(".comfy-node-body > div > div");
            if (el) {
                el.appendChild(uploadBtn);
            }

            return result;
        };
    }
});

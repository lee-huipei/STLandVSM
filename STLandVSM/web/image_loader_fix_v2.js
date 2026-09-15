import { app } from "../../../scripts/app.js";

// 浏览器能直接显示的格式（直接显示原文件；其余格式用自动生成的 PNG 预览）
const PREVIEWABLE_EXTS = ["png", "jpg", "jpeg", "bmp", "webp", "gif", "ico"];

const NODE_NAME = "UniversalImageLoader";

function extOf(name) {
    const i = name.lastIndexOf(".");
    return i >= 0 ? name.slice(i + 1).toLowerCase() : "";
}

function needPreview(name) {
    return !PREVIEWABLE_EXTS.includes(extOf(name));
}

// ComfyUI 全局 CSS 有 transition:all，会让预览/节点框尺寸变化带动画（拖动时"慢慢变小"）。
// 这里把所有 DOM widget 的过渡动画全部禁用（包括 ComfyUI 自建的外层容器）。
(function disableDomWidgetTransitions() {
    try {
        const style = document.createElement("style");
        style.textContent = ".dom-widget, .dom-widget * { transition: none !important; }";
        document.head.appendChild(style);
    } catch (e) { /* 忽略 */ }
})();

// 幂等包装：防止 setup 兜底 与 beforeRegisterNodeDef 重复包装
let wrapped = false;

function wrapNodeType(nodeType) {
    if (!nodeType || wrapped) return;
    wrapped = true;

    const origOnNodeCreated = nodeType.prototype.onNodeCreated;
    nodeType.prototype.onNodeCreated = function () {
        const result = origOnNodeCreated?.apply(this, arguments);
        const node = this;

        const imageWidget = node.widgets?.find(w => w.name === "image");
        if (!imageWidget) return result;

        // ===== 预览区（所有格式统一走这里，随节点大小伸缩） =====
        const container = document.createElement("div");
        container.style.cssText = "display:flex;flex-direction:column;gap:4px;padding:4px;box-sizing:border-box;width:100%;height:100%;align-items:center;transition:none;";

        const uploadBtn = document.createElement("button");
        uploadBtn.textContent = "📁 选择文件 (EXR/TIF/PNG...)";
        uploadBtn.style.cssText = "width:100%;padding:4px 8px;cursor:pointer;background:#333;color:#fff;border:1px solid #555;border-radius:3px;transition:none;";
        container.appendChild(uploadBtn); // 按钮在上

        const previewImg = document.createElement("img");
        // transition:none 关键：ComfyUI 全局 CSS 有 transition:all，
        // 不禁用的话高度变化带动画，拖动时节点框"慢慢变小"
        previewImg.style.cssText = "width:100%;object-fit:contain;border-radius:3px;display:none;cursor:pointer;margin:0 auto;transition:none;";
        previewImg.alt = "预览";
        previewImg.title = "点击选择文件";
        container.appendChild(previewImg); // 预览在下，紧贴按钮

        // 预览状态（独立变量，避免 computeSize 自引用节点大小导致反馈循环）
        let imgVisible = false;
        let previewMaxH = 150; // 期望预览高度，onResize 时跟随节点更新

        const getWidgetH = () => imgVisible ? (56 + previewMaxH) : 48;

        // DOM widget：由 ComfyUI 渲染系统管理位置/大小
        let domWidget = null;
        try {
            domWidget = node.addDOMWidget("stlandvsm_preview", "div", container, {
                serialize: false,
                hideOnZoom: false,
                getMinHeight: () => 48,
                getMaxHeight: () => 900,
                getHeight: () => getWidgetH(),
            });
            // 关键：computeSize 固定返回小值！
            // LiteGraph 拖动拉小时会用 computeSize 做最小高度限制，若这里联动节点高度
            // 会形成"追赶"（每帧慢慢变小）。固定 48 后拉小完全不受限、即时跟手。
            // 预览的弹性高度走 getHeight（渲染层），不参与 resize 限制。
            domWidget.computeSize = function (width) {
                return [width, 48];
            };
        } catch (e) {
            console.error("[ImageLoader] addDOMWidget 失败:", e);
        }

        const setPreview = (name, type) => {
            previewImg.onerror = null;
            previewImg.src = "/view?filename=" + encodeURIComponent(name) + "&type=" + type + "&subfolder=&rand=" + Date.now();
            previewImg.style.display = "block";
            previewImg.onerror = () => {
                if (type === "input") {
                    setPreview(name, "output"); // input 找不到再试 output
                } else {
                    previewImg.style.display = "none";
                }
            };
        };

        // 预览高度跟随节点高度（节点拉大预览变大，拉小变小）
        const syncPreviewHeight = () => {
            previewMaxH = Math.max(60, Math.min(node.size[1] - 140, 800));
            previewImg.style.maxHeight = previewMaxH + "px";
        };

        const updatePreview = async () => {
            const name = imageWidget.value;
            if (!name) {
                imgVisible = false;
                previewImg.style.display = "none";
                node.setSize([Math.max(node.size[0], 210), 130]); // 收缩到仅按钮高度
                app.graph?.setDirtyCanvas?.(true, true);
                return;
            }
            imgVisible = true;
            previewImg.style.display = "block";
            syncPreviewHeight();
            if (needPreview(name)) {
                // EXR/TIF 等：按需生成 PNG 预览后显示
                try {
                    await fetch("/stlandvsm/ensure_preview?filename=" + encodeURIComponent(name) + "&type=input&rand=" + Date.now());
                } catch (e) { /* 生成失败也尝试显示 */ }
                setPreview(name + ".preview.png", "input");
            } else {
                // PNG/JPG/BMP 等：直接显示原文件
                setPreview(name, "input");
            }
            // 用预览实际高度（getWidgetH）展开节点，不用 computeSize（它固定 48）
            node.setSize([Math.max(node.size[0], 210), getWidgetH() + 90]);
            app.graph?.setDirtyCanvas?.(true, true);
        };

        // 值变化（下拉选择）时更新预览
        const origCallback = imageWidget.callback;
        imageWidget.callback = function (value) {
            const r = origCallback?.apply(this, arguments);
            updatePreview();
            return r;
        };

        // 用户拖拽节点大小 → 预览高度跟随。
        // 注意：LiteGraph 拖动 resize 时直接改 node.size（不调 onResize），
        // 所以用 onDrawForeground 每帧检测高度变化（前台渲染每帧必触发，跟手）
        const origResize = node.onResize;
        node.onResize = function (...args) {
            if (imgVisible) {
                syncPreviewHeight();
                app.graph?.setDirtyCanvas?.(true, true);
            }
            return origResize?.apply(this, args);
        };

        // 轮询检测节点高度变化（不依赖渲染钩子——新版渲染器不调 onDrawForeground/onResize）
        let lastH = node.size[1];
        const pollTimer = setInterval(() => {
            if (imgVisible && node.size[1] !== lastH) {
                lastH = node.size[1];
                syncPreviewHeight();
            }
        }, 50);
        const origOnRemoved = node.onRemoved;
        node.onRemoved = function (...args) {
            clearInterval(pollTimer);
            return origOnRemoved?.apply(this, args);
        };

        // 兜底：每次节点重绘时检查值变化（部分环境仍会触发）
        let lastValue = imageWidget.value;
        const origDrawFG = node.onDrawForeground;
        node.onDrawForeground = function (...args) {
            const v = imageWidget.value;
            if (v !== lastValue) {
                lastValue = v;
                updatePreview();
            }
            if (imgVisible && node.size[1] !== lastH) {
                lastH = node.size[1];
                syncPreviewHeight();
            }
            return origDrawFG?.apply(this, args);
        };

        // ===== 上传逻辑（accept 包含 EXR/TIF，绕过原生限制） =====
        const doUpload = () => {
            const input = document.createElement("input");
            input.type = "file";
            input.accept = ".png,.jpg,.jpeg,.bmp,.tif,.tiff,.webp,.exr,.hdr,.gif,.ico,.dds,.psd,.tga";

            input.onchange = async () => {
                const file = input.files[0];
                if (!file) return;

                uploadBtn.textContent = "⏳ 上传中...";
                uploadBtn.disabled = true;

                try {
                    const formData = new FormData();
                    formData.append("image", file);
                    formData.append("type", "input");
                    formData.append("overwrite", "true");

                    const resp = await fetch("/upload/image", { method: "POST", body: formData });
                    if (!resp.ok) throw new Error("上传失败 " + resp.status);
                    const result = await resp.json();
                    const filename = result.name || file.name;

                    // 非浏览器格式：让后端先生成 PNG 预览
                    if (needPreview(filename)) {
                        try {
                            await fetch("/stlandvsm/ensure_preview?filename=" + encodeURIComponent(filename) + "&type=input&rand=" + Date.now());
                        } catch (e) { /* 预览生成失败不阻塞上传 */ }
                    }

                    // 更新下拉列表
                    if (!imageWidget.options.values.includes(filename)) {
                        imageWidget.options.values.push(filename);
                        imageWidget.options.values.sort();
                    }
                    imageWidget.value = filename;
                    if (origCallback) origCallback(filename);
                    updatePreview();

                    uploadBtn.textContent = "✅ " + filename;
                    setTimeout(() => { uploadBtn.textContent = "📁 选择文件 (EXR/TIF/PNG...)"; uploadBtn.disabled = false; }, 1500);
                } catch (err) {
                    uploadBtn.textContent = "❌ " + err.message;
                    setTimeout(() => { uploadBtn.textContent = "📁 选择文件 (EXR/TIF/PNG...)"; uploadBtn.disabled = false; }, 2000);
                }
            };
            input.click();
        };

        uploadBtn.onclick = doUpload;
        previewImg.onclick = doUpload;

        // ===== 替换原生 upload 按钮：点它也能选 EXR/TIF；隐藏它避免双按钮 =====
        const uploadWidget = node.widgets?.find(w => w.name === "upload");
        if (uploadWidget) {
            uploadWidget.callback = function () { doUpload(); };
            uploadWidget.hidden = true; // 只保留我们自己的按钮
        }

        setTimeout(updatePreview, 300);
        return result;
    };
}

app.registerExtension({
    name: "STLandVSM.ImageLoaderFix",
    async beforeRegisterNodeDef(nodeType, nodeData) {
        if (nodeData.name !== NODE_NAME) return;
        wrapNodeType(nodeType);
    },
    async setup() {
        // 兜底：aki 版扩展 JS 加载可能晚于节点定义注册，
        // beforeRegisterNodeDef 不会触发，这里手动包装 + 轮询等节点定义
        const tryWrap = () => {
            const nt = window.LiteGraph?.registered_node_types?.[NODE_NAME];
            if (nt) wrapNodeType(nt);
        };
        tryWrap();
        for (let i = 0; i < 10 && !wrapped; i++) {
            await new Promise(r => setTimeout(r, 300));
            tryWrap();
        }
    }
});

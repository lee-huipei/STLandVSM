# STLandVSM — ComfyUI 图像转 3D 模型节点

> 作者联系方式：**V18959848282**（微信）

---

## 📦 包含两个节点

本仓库包含两个 **ComfyUI 自定义节点**，需配合使用：

| 节点 | 文件夹 | 功能 |
|------|--------|------|
| **Comfy OIIO** | `comfy_oiio` | 将生成的深位图（灰度图/深度图）转换为高清 EXR 格式 |
| **STLandVSM** | `STLandVSM` | 接收 OIIO 转换后的 EXR 图片，生成 **STL / VSM** 3D 模型 |

---

## 🔧 安装方法

### 1. 放置节点

将 `comfy_oiio` 和 `STLandVSM` **两个文件夹** 完整复制到 ComfyUI 的 `custom_nodes\` 目录下：

```
ComfyUI/
└── custom_nodes/
    ├── comfy_oiio/     ← 复制这里
    └── STLandVSM/      ← 复制这里
```

> 📍 **节点位置图示**：请参考 [节点位置说明.png](节点位置说明.png)

### 2. 启动验证

复制完成后，直接启动 ComfyUI，节点会自动验证许可证。

启动后控制台输出以下信息即验证通过：
```
[STLandVSM] 许可证验证通过
```

---

## 🔌 节点使用说明

> 🔗 **接线图示**：请参考 [节点对接说明.png](节点对接说明.png)

### 工作流程

```
模型生成的灰度图 → Comfy OIIO（转 EXR）→ STLandVSM（转 STL/VSM）
```

**关键说明：**
- OIIO 接收的图像必须是 **模型生成的深位图（灰度图/深度图）**，不是普通照片
- OIIO 将其转换为高清 EXR 格式
- STLandVSM 接收 EXR 图片，输出 STL / VSM 3D 模型文件

### 可用节点列表

启动 ComfyUI 后，您可以在节点列表中找到：

| 节点名称 | 所属 |
|----------|------|
| STL & VSM Converter | STLandVSM |
| 安全3D预览桥接 | STLandVSM |
| GLB 预览 | STLandVSM |
| 文件夹选择器 | STLandVSM |
| 布尔开关 | STLandVSM |
| 格式选择器 | STLandVSM |
| OIIO SaveImage / OIIO LoadImage | comfy_oiio |

---

## 📄 许可证

**本节点为付费商业软件，未授权使用仅提供试用（带水印）。**

- 首次启动为 **7 天试用期**，试用期内可正常使用所有功能
- 试用期结束后需要购买正式许可证才能继续使用
- 许可证与机器绑定，请勿分享给他人

### 购买正式许可证

如需购买或续期许可证，请联系作者：

> **微信：V18959848282**

或参考 `使用说明.txt` 中的联系方式。

---

## ⚠️ 注意事项

1. 节点核心文件为加密保护（`.pyc`），请勿修改
2. `comfy_oiio` 节点依赖 OpenImageIO 库（ComfyUI 管理器会自动安装）
3. 如有问题，请通过微信联系作者
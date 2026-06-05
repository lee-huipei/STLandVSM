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

### 2. 安装许可证

STLandVSM 文件夹内附赠一年期许可证，在 `STLandVSM\一年许可证\` 中：

1. 打开 `STLandVSM\一年许可证\`
2. 双击 `install_license.bat`
3. 看到「安装成功」提示完成
4. 启动 ComfyUI，节点自动验证

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

## ❓ 常见问题

**Q: 提示许可证未找到？**
A: 请先安装 `STLandVSM\一年许可证\` 中的 `install_license.bat`。

**Q: 输出的模型不对？**
A: 确认输入给 OIIO 的是模型生成的深位图（灰度图），而非普通彩色图片。

**Q: 需要购买正式许可证？**
A: 请联系作者。详见下方。

---

## 📄 许可证

**本节点为付费商业软件，未授权使用仅提供试用（带水印）。**

- 附赠的一年期许可证从第一次启动 ComfyUI 开始计时
- 到期后可联系我们续期
- 许可证文件与机器绑定，请勿分享给他人

### 购买正式许可证

如需购买或续期许可证，请联系作者：

> **微信：V18959848282**

或参考 `使用说明.txt` 中的联系方式。

---

## ⚠️ 注意事项

1. 节点核心文件为加密保护（`.pyc`），请勿修改
2. `comfy_oiio` 节点依赖 OpenImageIO 库
3. 请定期备份您的许可证文件
4. 如有问题，请通过微信联系作者

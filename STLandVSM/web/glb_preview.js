import { app } from "../../../scripts/app.js";

const THREE_BASE = "/extensions/STLandVSM/three/";

async function loadTHREE() {
    if (window.__STL_THREE) return window.__STL_THREE;

    const scripts = [
        THREE_BASE + "three.min.js",
        THREE_BASE + "GLTFLoader.js",
        THREE_BASE + "OrbitControls.js",
    ];

    for (const src of scripts) {
        await new Promise((resolve, reject) => {
            const s = document.createElement("script");
            s.src = src;
            s.onload = resolve;
            s.onerror = () => reject(new Error("加载失败: " + src));
            document.head.appendChild(s);
        });
    }

    window.__STL_THREE = true;
    console.log("[GLB预览] Three.js 加载完成");
    return window.THREE;
}

const THREE = await loadTHREE();
const GLTFLoader = THREE.GLTFLoader;
const OrbitControls = THREE.OrbitControls;
const {
    Scene, PerspectiveCamera, WebGLRenderer,
    AmbientLight, DirectionalLight,
    GridHelper,
    MeshStandardMaterial, DoubleSide,
    BufferAttribute,
    Box3, Vector3, Color,
    PlaneGeometry, Mesh,
} = THREE;

app.registerExtension({
    name: "STLandVSM.GLBPreview",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name !== "GLBPreview") return;

        const onNodeCreated = nodeType.prototype.onNodeCreated;
        nodeType.prototype.onNodeCreated = async function () {
            const result = onNodeCreated?.apply(this, arguments);
            const node = this;

            let currentMode = "实体";
            const modeWidget = node.widgets?.find(w => w.name === "显示模式");
            if (modeWidget) {
                setTimeout(() => {
                    if (!modeWidget.value || modeWidget.value === "") {
                        modeWidget.value = "彩色地形";
                        if (modeWidget.callback) modeWidget.callback("彩色地形");
                        currentMode = "彩色地形";
                        if (currentModel) applyMaterial(currentModel, "彩色地形");
                        app.graph.setDirtyCanvas(true, false);
                    }
                }, 500);
                currentMode = modeWidget.value || "实体";
                modeWidget.callback = (v) => {
                    currentMode = v;
                    if (currentModel) applyMaterial(currentModel, currentMode);
                };
            }

            const container = document.createElement("div");
            container.style.width = "100%";
            container.style.height = "100%";
            container.style.minHeight = "30px";
            container.style.minWidth = "30px";
            container.style.background = "#1a1a2e";
            container.style.borderRadius = "8px";
            container.style.position = "relative";
            container.style.willChange = "transform";
            container.style.contain = "none";

            node.addDOMWidget("viewer", "canvas", container, { serialize: false, hideOnZoom: false });

            let scene, camera, renderer, controls, currentModel;
            let width = 400, height = 300;

            function applyMaterial(model, mode) {
                if (!model) return;
                if (mode === "实体") {
                    model.traverse((child) => {
                        if (child.isMesh && child.material) {
                            const mat = child.material;
                            if (mat.color) mat.color.set(0xD2B48C);
                            if (mat.roughness !== undefined) mat.roughness = 0.15;
                            if (mat.metalness !== undefined) mat.metalness = 0.0;
                            if (mat.emissive) mat.emissive.set(0x000000);
                            mat.vertexColors = false;
                            mat.needsUpdate = true;
                            child.castShadow = true;
                            child.receiveShadow = true;
                        }
                    });
                } else if (mode === "彩色地形") {
                    model.traverse((child) => {
                        if (child.isMesh && child.geometry && child.geometry.attributes.position) {
                            const positions = child.geometry.attributes.position.array;
                            const vertexCount = positions.length / 3;
                            let minZ = Infinity, maxZ = -Infinity;
                            for (let i = 0; i < vertexCount; i++) {
                                const z = positions[i * 3 + 2];
                                if (z < minZ) minZ = z;
                                if (z > maxZ) maxZ = z;
                            }
                            const range = maxZ - minZ;
                            const colors = [];
                            for (let i = 0; i < vertexCount; i++) {
                                const z = positions[i * 3 + 2];
                                let t = range > 0 ? (z - minZ) / range : 0;
                                if (z - minZ < 0.01) {
                                    colors.push(0.2, 0.2, 0.25);
                                } else {
                                    t = Math.max(0, Math.min(1, t));
                                    let r, g, b;
                                    if (t < 0.5) {
                                        const s = t / 0.5;
                                        r = 0.145 + s * 0.153;
                                        g = 0.365 + s * 0.290;
                                        b = 0.400 - s * 0.055;
                                        const mid = 1 - Math.abs(s - 0.5) * 2;
                                        r += mid * 0.3; g += mid * 0.3; b += mid * 0.3;
                                    } else {
                                        const s = (t - 0.5) / 0.5;
                                        r = 0.298 + s * 0.416;
                                        g = 0.655 - s * 0.110;
                                        b = 0.345;
                                    }
                                    colors.push(r, g, b);
                                }
                            }
                            child.geometry.setAttribute("color", new BufferAttribute(new Float32Array(colors), 3));
                            const mat = child.material;
                            if (mat) {
                                mat.vertexColors = true;
                                mat.roughness = 0.15;
                                mat.metalness = 0.0;
                                if (mat.emissive) mat.emissive.set(0x000000);
                                mat.needsUpdate = true;
                            }
                            child.castShadow = true;
                            child.receiveShadow = true;
                        }
                    });
                }
            }

            function init() {
                scene = new Scene();
                scene.background = new Color(0x1a1a2e);
                camera = new PerspectiveCamera(40, 1, 0.1, 1000);
                camera.position.set(4, 3, 5);
                camera.lookAt(0, 0, 0);

                renderer = new WebGLRenderer({ antialias: true });
                renderer.setSize(width, height);
                renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
                container.appendChild(renderer.domElement);

                renderer.shadowMap.enabled = true;
                renderer.shadowMap.type = 2;

                scene.add(new AmbientLight(0xffffff, 0.5));

                const lightSetup = [
                    { pos: [0, 10, 10],  intensity: 0.8 },
                    { pos: [0, 10, -10], intensity: 0.5 },
                    { pos: [-10, 0, 0],  intensity: 0.3 },
                    { pos: [10, 0, 0],   intensity: 0.3 },
                    { pos: [0, -10, 0],  intensity: 0.2 },
                ];
                for (const l of lightSetup) {
                    const light = new DirectionalLight(0xffffff, l.intensity);
                    light.position.set(l.pos[0], l.pos[1], l.pos[2]);
                    if (l.intensity >= 0.5) {
                        light.castShadow = true;
                        light.shadow.mapSize.width = 1024;
                        light.shadow.mapSize.height = 1024;
                        light.shadow.camera.near = 0.5;
                        light.shadow.camera.far = 50;
                        light.shadow.camera.left = -8;
                        light.shadow.camera.right = 8;
                        light.shadow.camera.top = 8;
                        light.shadow.camera.bottom = -8;
                        light.shadow.bias = -0.001;
                    }
                    scene.add(light);
                }

                const grid = new GridHelper(20, 20, 0x555577, 0x333355);
                grid.position.y = 0;
                scene.add(grid);

                const floor = new Mesh(
                    new PlaneGeometry(24, 24),
                    new MeshStandardMaterial({
                        color: 0x12121e, transparent: true, opacity: 0.5,
                        roughness: 1.0, metalness: 0.0, side: DoubleSide,
                    })
                );
                floor.rotation.x = -Math.PI / 2;
                floor.position.y = -0.01;
                floor.receiveShadow = true;
                scene.add(floor);

                if (OrbitControls) {
                    controls = new OrbitControls(camera, renderer.domElement);
                    controls.enableDamping = true;
                    controls.minDistance = 1;
                    controls.maxDistance = 50;
                }
                animate();
            }

            function checkSize() {
                const newW = Math.round(container.offsetWidth);
                const newH = Math.round(container.offsetHeight);
                if (newW > 0 && newH > 0 && (newW !== width || newH !== height)) {
                    width = newW; height = newH;
                    camera.aspect = width / height;
                    camera.updateProjectionMatrix();
                    renderer?.setSize(width, height);
                }
            }

            function animate() {
                checkSize();
                if (controls) controls.update();
                if (renderer && scene && camera) renderer.render(scene, camera);
                requestAnimationFrame(animate);
            }

            function loadGLB(url) {
                if (currentModel) { scene.remove(currentModel); currentModel = null; }
                if (!url || url === "") return;

                const loader = new GLTFLoader();
                loader.load(url, (gltf) => {
                    currentModel = gltf.scene;
                    scene.add(currentModel);
                    applyMaterial(currentModel, currentMode);

                    const box = new Box3().setFromObject(currentModel);
                    const center = box.getCenter(new Vector3());
                    const minY = box.min.y;
                    currentModel.position.x -= center.x;
                    currentModel.position.y -= minY;
                    currentModel.position.z -= center.z;

                    const newBox = new Box3().setFromObject(currentModel);
                    const newSize = newBox.getSize(new Vector3());
                    const maxDim = Math.max(newSize.x, newSize.y, newSize.z);
                    if (maxDim > 0) {
                        const distance = maxDim * 2.2;
                        camera.position.set(distance * 0.7, distance * 0.55, distance * 0.85);
                        camera.lookAt(0, newSize.y * 0.35, 0);
                        if (controls) { controls.target.set(0, newSize.y * 0.35, 0); controls.update(); }
                    }
                }, undefined, (err) => {
                    console.error("[GLB预览] 加载失败:", err);
                });
            }

            init();

            // 首次加载品牌模型
            async function loadInitialModel() {
                const ts = Date.now();
                loadGLB("/view?filename=branding.glb&type=output&subfolder=glb_preview&ts=" + ts);
            }
            loadInitialModel();

            // 监听队列完成
            app.api?.addEventListener?.("executed", function globalHandler(event) {
                const data = event.detail;
                if (!data) return;
                let foundFile = null;
                function search(v) {
                    if (foundFile) return;
                    if (typeof v === 'string') {
                        const m = v.match(/([^\\\/\s,)'"]+\.glb)/i);
                        if (m) foundFile = m[1];
                    } else if (Array.isArray(v)) {
                        v.forEach(search);
                    } else if (v && typeof v === 'object') {
                        Object.values(v).forEach(search);
                    }
                }
                search(data.output || data.result || []);
                if (foundFile) {
                    loadGLB("/view?filename=" + encodeURIComponent(foundFile) + "&type=output&subfolder=glb_preview&ts=" + Date.now());
                }
            });

            return result;
        };
    }
});

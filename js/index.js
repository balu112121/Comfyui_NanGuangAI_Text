import { app } from "../../../scripts/app.js";

// 全局样式（灰色占位符）
const style = document.createElement('style');
style.textContent = `
    .nanguang-placeholder::placeholder {
        color: #999 !important;
        font-size: 14px !important;
        font-style: italic !important;
        opacity: 0.8 !important;
    }
`;
document.head.appendChild(style);

// 设置占位符的函数
function setPlaceholder(node) {
    if (!node.widgets) return;
    for (let w of node.widgets) {
        if (w.type === 'text' || w.type === 'textarea') {
            // 优先使用 inputEl（ComfyUI 1.0+），否则回退到 element
            const el = w.inputEl || w.element;
            if (el && (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA')) {
                // 从节点定义中读取 placeholder 属性
                const config = node.constructor?.nodeData?.input?.required?.text?.[1];
                if (config && config.placeholder) {
                    if (!el.placeholder) {
                        el.placeholder = config.placeholder;
                        el.classList.add('nanguang-placeholder');
                        el.style.color = '#333';
                    }
                }
            }
        }
    }
}

// 遍历所有现有节点
function applyToAllNodes() {
    for (let node of app.graph.nodes) {
        setPlaceholder(node);
    }
}

// 注册扩展
app.registerExtension({
    name: "Comfyui_NanGuangAI_Text",
    init() {
        // 工作流加载完成后应用
        app.graph.on("afterConfigure", () => {
            setTimeout(applyToAllNodes, 300);
        });

        // 新节点添加时应用
        app.graph.on("nodeAdded", (node) => {
            setTimeout(() => setPlaceholder(node), 300);
        });

        // 节点复制/粘贴时触发
        app.graph.on("nodeChanged", (node) => {
            if (node.type && node.type.startsWith('NanGuangAI_')) {
                setTimeout(() => setPlaceholder(node), 200);
            }
        });
    }
});
class BaseNanGuangText:
    """基础节点，提供文本输入和帮助输出"""
    placeholder = ""  # 子类重写

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "dynamicPrompts": False,
                    "placeholder": cls.placeholder,  # 关键：占位符随节点定义传递
                }),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("提示词文本", "帮助信息")
    FUNCTION = "process"
    CATEGORY = "南光AI/文本"

    def process(self, text):
        help_text = "南光AIGC提示词节点：请将提示词文本连接到后续图像生成或编辑节点使用。"
        return (text, help_text)


class NanGuangAI_Text(BaseNanGuangText):
    placeholder = "南光AIGC温馨提示：请输入图像编辑提示词"


class NanGuangAI_Text_Positive(BaseNanGuangText):
    placeholder = "南光AIGC温馨提示：请输入正向提示词"


class NanGuangAI_Text_Negative(BaseNanGuangText):
    placeholder = "南光AIGC温馨提示：请输入负向提示词"
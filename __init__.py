import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from .nodes import NanGuangAI_Text, NanGuangAI_Text_Positive, NanGuangAI_Text_Negative

NODE_CLASS_MAPPINGS = {
    "NanGuangAI_Text": NanGuangAI_Text,
    "NanGuangAI_Text_Positive": NanGuangAI_Text_Positive,
    "NanGuangAI_Text_Negative": NanGuangAI_Text_Negative,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NanGuangAI_Text": "南光AI提示词-编辑文本",
    "NanGuangAI_Text_Positive": "南光AI提示词-正向提示词文本",
    "NanGuangAI_Text_Negative": "南光AI提示词-负向提示词文本",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
WEB_DIRECTORY = "./js"
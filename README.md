# comfyui_random_p
random prompt easy useable for comfyui
ComfyUI自定义节点，提供动态提示词组合功能。

## Functional Features 功能特性
- 从多行文本中随机选择提示词片段
- 支持与上游提示词内容智能合并
- 提示文本可以用“,”分隔，也可以换行分隔
- 可设置固定种子保证结果可复现
- 
- Randomly selects prompt word fragments from multiple lines of text
- Supports intelligent merging with upstream prompt content
- Prompt text can be separated by commas or line breaks
- Fixed seeds can be set to ensure reproducible results

## Installation Method 安装方法
1. Copy the comfyui_random_p.py file to the custom_nodes directory of ComfyUI；将 `comfyui_random_p.py` 复制到 ComfyUI 的 `custom_nodes` 目录
2. Restart the ComfyUI service；重启 ComfyUI 服务

## Usage Example 使用示例
```python
{
  "prompt": [{
    "inputs": {
      "seed": 0,
      "custom_prompts": "sunset, moonrise\ncloudy, rainy"
    },
    "class_type": "RandomPromptNode"
  }]
}

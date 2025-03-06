import random
import comfy.utils

class RandomPromptNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, 
                        "description": "0=随机，非0=固定"}),  # 合并模式控制
                "custom_prompts": ("STRING", {
                    "multiline": True, 
                    "default": "dog, cat\nbird, rabbit\nmoon"
                }),
            },
            "optional": {
                "prev_prompt": ("STRING", {"forceInput": True}),  # 上游提示词（可选）
            }
        }

    RETURN_TYPES = ("STRING", "INT")
    RETURN_NAMES = ("prompt", "seed")
    FUNCTION = "get_prompt"

    def get_prompt(self, seed, custom_prompts, prev_prompt=None):
        # 当且仅当上游节点实际连接且未被忽略时合并内容
        base_prompt = prev_prompt.strip() if (prev_prompt is not None and prev_prompt.strip()) else ""
        
        prompts = [
            p.strip() 
            for line in custom_prompts.split('\n')
            for p in line.split(',') 
            if p.strip()
        ]
        
        selected = random.choice(prompts) if prompts else ""
        
        final_seed = seed if seed != 0 else random.randint(1, 0xffffffffffffffff)
        
        # 最终合并逻辑：仅当base_prompt有效时拼接
        final_prompt = f"{base_prompt} {selected}".strip() if base_prompt else selected
        
        return (final_prompt, final_seed)

    # ==== 删除重复代码 ====

# 节点注册
NODE_CLASS_MAPPINGS = {
    "random_p": RandomPromptNode  # 修改键名控制节点调用名称
}

# 显示名称映射
NODE_DISPLAY_NAME_MAPPINGS = {
    "random_p": "random p"  # 键名与CLASS映射一致，值控制界面显示名称
}
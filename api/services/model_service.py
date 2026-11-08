from typing import Any

class ModelService:
    """Small adapter around a Hugging Face text-generation pipeline."""
    def __init__(self, model_id: str = "HuggingFaceTB/SmolLM2-360M", generator: Any = None):
        self.model_id = model_id
        self.generator = generator

    def load(self, device: str = "auto") -> None:
        import torch
        from transformers import pipeline
        kwargs = {"device_map": "auto"} if device == "auto" else {"device": device}
        self.generator = pipeline("text-generation", model=self.model_id,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32, **kwargs)

    def generate(self, prompt: str, max_new_tokens: int = 128, temperature: float = 0.7) -> str:
        if self.generator is None:
            raise RuntimeError("Model is not loaded")
        options = {"max_new_tokens": max_new_tokens, "do_sample": temperature > 0}
        if temperature > 0:
            options["temperature"] = temperature
        result = self.generator(prompt, **options)
        text = result[0]["generated_text"]
        return text[len(prompt):].strip() if text.startswith(prompt) else text.strip()

# app/services/llm/llama3.py

import subprocess
from app.services.llm.base_llm import BaseLLM

class LlamaMunicipal(BaseLLM):
    @property
    def name(self) -> str:
        return "LLaMA Municipal"

    def _call_model(self, texto: str) -> str:
        result = subprocess.run(
            ["ollama", "run", "llama-municipal"],
            input=texto,
            text=True,
            encoding="utf-8",
            capture_output=True,
            timeout=300
        )
        return result.stdout.strip()

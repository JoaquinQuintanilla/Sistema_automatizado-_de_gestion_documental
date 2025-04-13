# app/services/llm/deepseek.py

import subprocess
import json
import re
from app.services.llm.base_llm import BaseLLM

class DeepseekMunicipal(BaseLLM):
    @property
    def name(self) -> str:
        return "DeepSeek-Municipal"

    def analyze_text(self, texto: str) -> dict:
        prompt = texto.strip()
        try:
            result = subprocess.run(
                ["ollama", "run", "deepseek-municipal"],
                input=prompt,
                text=True,
                encoding="utf-8",
                capture_output=True,
                timeout=300,
            )
            output = result.stdout.strip()

            match = re.search(r"```json\s*(\{.*?\})\s*```", output, re.DOTALL)
            if not match:
                match = re.search(r"(\{.*\})", output, re.DOTALL)

            if match:
                json_str = match.group(1)
                json_str = re.sub(r"//.*", "", json_str)  # Eliminar comentarios tipo //
                return json.loads(json_str)

            raise ValueError(f"Respuesta inválida de LLaMA (no es JSON):\n{output}")

        except json.JSONDecodeError as e:
            raise ValueError(f"Error al decodificar JSON: {e}\nRespuesta:\n{output}")
        except Exception as e:
            raise RuntimeError(f"Error al ejecutar el modelo DeepSeek-Municipal: {str(e)}")

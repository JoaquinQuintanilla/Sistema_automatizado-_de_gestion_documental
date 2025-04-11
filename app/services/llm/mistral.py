# app/services/llm/mistral.py

from app.services.llm.base_llm import BaseLLM
import subprocess
import json
import re

class MistralMunicipal(BaseLLM):
    def __init__(self):
        self.model_name = "mistral-municipal"

    @property
    def name(self) -> str:
        return "Mistral 7B Municipal"

    def analyze_text(self, text: str) -> dict:
        prompt = f"{text}"
        try:
            result = subprocess.run(
                ["ollama", "run", self.model_name],
                input=prompt,
                text=True,
                encoding="utf-8",
                capture_output=True,
                timeout=300
            )
            output = result.stdout.strip()

            match = re.search(r"```json\s*(\{.*?\})\s*```", output, re.DOTALL)
            if not match:
                match = re.search(r"(\{.*\})", output, re.DOTALL)

            if match:
                json_str = match.group(1)
                # Limpieza: eliminar comentarios tipo `// ...`
                json_str = re.sub(r"//.*", "", json_str)
                return json.loads(json_str)

            raise ValueError(f"Respuesta inválida de LLaMA (no es JSON):\n{output}")

        except json.JSONDecodeError as e:
            raise ValueError(f"Error al decodificar JSON: {e}\nRespuesta:\n{output}")
        except Exception as e:
            raise RuntimeError(f"Error al ejecutar el modelo {self.model_name}: {str(e)}")

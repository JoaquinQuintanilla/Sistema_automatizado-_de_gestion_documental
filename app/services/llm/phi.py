import re
import json
import subprocess
from app.services.llm.base_llm import BaseLLM

class PhiMunicipal(BaseLLM):
    def __init__(self):
        self.model_name = "phi-municipal"

    @property
    def name(self) -> str:
        return "Phi Municipal"

    def analyze_text(self, text: str) -> dict:
        prompt = text.strip()
        try:
            result = subprocess.run(
                ["ollama", "run", self.model_name],
                input=prompt,
                text=True,
                encoding="utf-8",
                capture_output=True,
                timeout=90
            )
            output = result.stdout.strip()

            match = re.search(r"```json\s*(.*?)```", output, re.DOTALL)
            if match:
                output = match.group(1).strip()

            output_sin_comentarios = re.sub(r"//.*", "", output)

            return json.loads(output_sin_comentarios)

        except json.JSONDecodeError as e:
            raise ValueError(f"Error al decodificar JSON: {e}\nRespuesta:\n{output}")

        except Exception as e:
            raise RuntimeError(f"Error al ejecutar el modelo {self.model_name}: {str(e)}")

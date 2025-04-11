# app/services/llm/llama3.py

import subprocess
import json
import re
from app.services.llm.base_llm import BaseLLM

class Llama3Municipal(BaseLLM):
    @property
    def name(self) -> str:
        return "LLaMA 3.2 Municipal"

    def analyze_text(self, texto: str) -> dict:
        prompt = texto.strip()

        try:
            result = subprocess.run(
                ["ollama", "run", "llama3.2-municipal"],
                input=prompt,
                text=True,
                encoding="utf-8",
                capture_output=True,
                timeout=300
            )

            output = result.stdout.strip()

            # Buscar bloque JSON entre ```json ... ```
            match = re.search(r"```json\s*(\{.*?\})\s*```", output, re.DOTALL)
            if not match:
                match = re.search(r"(\{.*\})", output, re.DOTALL)

            if match:
                json_text = re.sub(r"//.*", "", match.group(1))
                return json.loads(json_text)

            raise ValueError(f"Respuesta inválida de LLaMA (no es JSON):\n{output}")

        except json.JSONDecodeError as e:
            raise ValueError(f"Error al decodificar JSON: {e}\nRespuesta:\n{output}")
        except Exception as e:
            raise RuntimeError(f"Error al ejecutar modelo LLaMA: {str(e)}")

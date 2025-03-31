# app/services/llm/llama3.py

import subprocess
import json
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
                input=prompt.encode("utf-8"),
                capture_output=True,
                timeout=90
            )

            if result.returncode != 0:
                raise RuntimeError(f"Ollama error: {result.stderr.decode()}")

            output = result.stdout.decode().strip()

            # 🔧 Limpieza de delimitadores tipo Markdown ```json ... ```
            if output.startswith("```json"):
                output = output.removeprefix("```json").strip()
            if output.endswith("```"):
                output = output.removesuffix("```").strip()

            # ✅ Intenta parsear el JSON limpio
            return json.loads(output)

        except json.JSONDecodeError:
            raise ValueError(f"Respuesta inválida de LLaMA (no es JSON):\n{output}")

        except Exception as e:
            raise RuntimeError(f"Error al ejecutar modelo LLaMA: {str(e)}")

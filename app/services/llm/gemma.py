import re
import json
import subprocess
from app.services.llm.base_llm import BaseLLM
from datetime import datetime

class GemmaMunicipal(BaseLLM):
    def __init__(self):
        self.model_name = "gemma-municipal"

    @property
    def name(self) -> str:
        return "gemma Municipal"

    def analyze_text(self, text: str) -> dict:
        prompt = text.strip()

        try:
            # Forzar reinicio limpio del modelo con --system vacío para resetear contexto
            result = subprocess.run(
                ["ollama", "run", self.model_name],
                input=prompt.encode("utf-8"),
                capture_output=True,
                timeout=300
            )

            output = result.stdout.decode("utf-8").strip()

            # Validación temprana: el modelo debe responder un JSON válido
            if not output.startswith("{") and "```json" not in output:
                self._log_error(prompt, output)
                raise ValueError(f"Respuesta no válida: no es JSON. Salida:\n{output}")

            # Si viene encerrado entre ```json ... ```
            match = re.search(r"```json\s*(.*?)```", output, re.DOTALL)
            if match:
                output = match.group(1).strip()

            # Eliminar comentarios tipo "//..."
            output_sin_comentarios = re.sub(r"//.*", "", output)

            return json.loads(output_sin_comentarios)

        except json.JSONDecodeError as e:
            self._log_error(prompt, output)
            raise ValueError(f"Error al decodificar JSON: {e}\nRespuesta:\n{output}")

        except Exception as e:
            raise RuntimeError(f"Error al ejecutar el modelo {self.model_name}: {str(e)}")

    def _log_error(self, prompt: str, output: str):
        """Guardar errores en un log para revisión manual."""
        with open("errores_gemma.log", "a", encoding="utf-8") as log:
            log.write(f"\n\n===== ERROR @ {datetime.now()} =====\n")
            log.write("PROMPT:\n")
            log.write(prompt + "\n")
            log.write("OUTPUT:\n")
            log.write(output + "\n")

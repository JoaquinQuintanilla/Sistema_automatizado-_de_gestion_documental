from abc import ABC, abstractmethod
import json
import re

class BaseLLM(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Nombre del modelo."""
        pass

    @abstractmethod
    def _call_model(self, texto: str) -> str:
        """
        Ejecuta el modelo con el texto de entrada y retorna la respuesta completa como string.
        
        Args:
            texto (str): Texto completo del documento.

        Returns:
            str: Respuesta cruda del modelo.
        """
        pass

    def analyze_text(self, texto: str) -> dict:
        """
        Ejecuta el modelo y extrae un diccionario JSON limpio desde la respuesta.
        
        Args:
            texto (str): Texto procesado por OCR u otra fuente.

        Returns:
            dict: Diccionario con los metadatos extraídos.
        """
        output = self._call_model(texto.strip())
        return self._extract_json(output)

    def _extract_json(self, output: str) -> dict:
        """
        Extrae y limpia el bloque JSON desde una respuesta de modelo LLM.

        Args:
            output (str): Texto crudo del modelo.

        Returns:
            dict: JSON válido como diccionario.
        """
        match = re.search(r"```json\s*(\{.*?\})\s*```", output, re.DOTALL)
        if not match:
            match = re.search(r"(\{.*\})", output, re.DOTALL)

        if not match:
            raise ValueError(f"Respuesta inválida del modelo (no contiene JSON):\n{output}")

        json_text = match.group(1)

        # Arregla comillas escapadas
        json_text = json_text.replace('\\"', '"')

        # Agrega llave de cierre si falta
        if json_text.count("{") > json_text.count("}"):
            json_text += "}"

        # Elimina barras innecesarias mal escapadas
        json_text = re.sub(r'(?<!\\)\\(?!["\\/bfnrtu])', '', json_text)

        try:
            parsed = json.loads(json_text)
            return self._try_parse_json_strings(parsed)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error al decodificar JSON: {e}\nRespuesta:\n{output}")

    def _try_parse_json_strings(self, obj):
        """
        Convierte recursivamente strings JSON embebidos dentro de un dict o lista en objetos reales.

        Args:
            obj (dict | list): Objeto JSON ya parseado.

        Returns:
            dict | list: Objeto JSON con subniveles convertidos.
        """
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, str):
                    try:
                        parsed = json.loads(value)
                        obj[key] = self._try_parse_json_strings(parsed)
                    except json.JSONDecodeError:
                        pass
                elif isinstance(value, (dict, list)):
                    obj[key] = self._try_parse_json_strings(value)
        elif isinstance(obj, list):
            for i in range(len(obj)):
                obj[i] = self._try_parse_json_strings(obj[i])
        return obj

from abc import ABC, abstractmethod

class BaseLLM(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Nombre del modelo."""
        pass

    @abstractmethod
    def analyze_text(self, texto: str) -> dict:
        """
        Procesa un texto y devuelve un diccionario con los resultados extraídos.
        
        Args:
            texto (str): Texto completo del documento.

        Returns:
            dict: Diccionario con los metadatos extraídos.
        """
        pass


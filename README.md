
# Proyecto de Título - Sistema Automatizado de Gestión Documental

## Descripción
Este proyecto implementa un **sistema automatizado de gestión documental** para la Municipalidad de Valparaíso, utilizando **inteligcia artificial**.

El sistema permite digitalizar, clasificar y extraer información clave de documentos municipales mediante modelos avanzados de **OCR** y **modelos de lenguaje a gran escala (LLMs)**. La solución se expone a través de una **API REST**, generando resultados en formato JSON para garantizar interoperabilidad.

## Tecnologías Utilizadas
- **Framework API**: FastAPI
- **OCR**: Tesseract, EasyOCR, PaddleOCR, Donut (opcional)
- **LLMs**: LLaMA 3, DistilLLaMA, Mistral, Phi
- **Gestor de Dependencias**: pip / virtualenv
- **Control de Versiones**: Git
- **Metodología**: Scrum
- **Motor de LLMs local**: Ollama + modelo personalizado `llama3.2-municipal`

## Estructura del Proyecto
```
proyecto_titulo/
├── app/
│   ├── api/
│   │   ├── endpoints.py        # Endpoints de la API REST
│   │   ├── schemas.py          # Modelos de datos con Pydantic
│   ├── core/
│   │   ├── config.py           # Configuración global
│   │   ├── logger.py           # Registro de logs
│   ├── services/
│   │   ├── ocr/
│   │   │   ├── base_ocr.py     # Clase base para OCR
│   │   │   ├── tesseract.py    # OCR con Tesseract
│   │   │   ├── easyocr.py      # OCR con EasyOCR
│   │   │   ├── paddleocr.py    # OCR con PaddleOCR
│   │   │   ├── donut.py        # OCR con Donut (opcional)
│   │   ├── llm/
│   │   │   ├── base_llm.py     # Clase base para LLMs
│   │   │   ├── llama3.py       # Modelo LLaMA 3 personalizado (Ollama)
│   │   │   ├── distil_llama.py # Versión ligera de LLaMA
│   │   │   ├── mistral.py      # Modelo Mistral
│   │   │   ├── phi.py          # Modelo Phi
│   ├── utils/
│   │   ├── file_utils.py       # Utilidades para manejo de archivos
│   │   ├── metrics.py          # Evaluación del rendimiento
├── models/
│   ├── llama3.2-municipal/
│   │   ├── Modelfile           # Configuración personalizada del modelo LLaMA
├── tests/                      # Pruebas unitarias
├── requirements.txt            # Dependencias del proyecto
├── README.md                   # Documentación
├── .gitignore                  # Archivos a ignorar en Git
```

## Instalación y Configuración
1. Clonar el repositorio:
   ```sh
   git clone https://github.com/usuario/proyecto_titulo.git
   cd proyecto_titulo
   ```
2. Crear y activar un entorno virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```
3. Instalar dependencias:
   ```sh
   pip install -r requirements.txt
   ```
4. Configurar variables de entorno en `app/core/config.py` o mediante un archivo `.env`.

## Uso
Ejecutar la API con FastAPI:
```sh
uvicorn app.main:app --reload
```
La documentación de la API estará disponible en:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## LLM personalizado con Ollama
Para construir el modelo `llama3.2-municipal` utilizado por el sistema:

```sh
cd models/llama3.2-municipal
ollama create llama3.2-municipal -f Modelfile
```

Luego puedes probarlo manualmente con:
```sh
ollama run llama3.2-municipal
```

Este modelo ha sido afinado con un prompt especializado para extraer metadatos estructurados desde documentos municipales en español, cumpliendo con la normativa chilena vigente.

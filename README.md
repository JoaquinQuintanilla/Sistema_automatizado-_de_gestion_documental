# Proyecto de Título - Sistema Automatizado de Gestión Documental

## Descripción

Este proyecto implementa un **sistema automatizado de gestión documental** para la Municipalidad de Valparaíso, utilizando técnicas de **inteligencia artificial**.

El sistema permite digitalizar, clasificar y extraer información clave de documentos municipales mediante modelos avanzados de **OCR** y **modelos de lenguaje a gran escala (LLMs)**. La solución se expone a través de una **API REST**, generando resultados en formato JSON estructurado, cumpliendo con la Ley 21.180 sobre Transformación Digital del Estado.

## Tecnologías Utilizadas

- **Framework API**: FastAPI  
- **OCR**: Tesseract, EasyOCR, PaddleOCR
- **LLMs**: LLaMA 3, Mistral, DeepSeek, Qwen, Gemma  
- **Gestor de Dependencias**: pip / virtualenv  
- **Control de Versiones**: Git  
- **Motor de LLMs local**: Ollama  
- **Metodología**: Scrum  

## Estructura del Proyecto

```
proyecto_titulo/
├── app/
│   ├── api/               # Endpoints y modelos de entrada/salida
│   ├── core/              # Configuraciones y logger
│   ├── services/          # Implementación de OCRs y LLMs
│   └── utils/             # Métricas y utilidades
├── models/                # Archivos de configuración de modelos Ollama
├── tests/                 # Pruebas unitarias
├── resultados/graficos/  # Visualizaciones generadas por Jupyter
├── requirements.txt
├── README.md
└── .gitignore
```

## Instalación y Configuración

```bash
git clone https://github.com/usuario/proyecto_titulo.git
cd proyecto_titulo
python -m venv venv
source venv/bin/activate  # O venv\Scripts\activate en Windows
pip install -r requirements.txt
```

## Ejecución

```bash
uvicorn app.main:app --reload
```

- Documentación Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Resultados y Evaluación

Se evaluaron 15 combinaciones posibles de OCR y LLM utilizando más de **9,000 documentos municipales**. A partir de los resultados recolectados se concluyó que:

-  El **OCR más eficiente y preciso** es **PaddleOCR**, tanto en uso de CPU como en tiempo de ejecución.
-  Los **LLMs más eficientes en tiempo y precisión** son **LLaMA 3.2 (3B)** y **Qwen2.5 (3B)**.
-  Las **combinaciones más rápidas** y con buen rendimiento global fueron:
  - `paddleocr_llama3`
  - `paddleocr_qwen`

Además, se evaluó la capacidad de cada LLM para extraer clasificadores desde los documentos municipales, con un promedio de más de **13 clasificadores por documento** en los mejores modelos.

Para visualizar los resultados en detalle, consulta: [`README_graficos.md`](./resultados/graficos/README_graficos.md)

---

## Construcción del Modelo LLaMA Municipal

```bash
cd models/llama3.2-municipal
ollama create llama3.2-municipal -f Modelfile
ollama run llama3.2-municipal
```

Este modelo personalizado fue optimizado para extraer metadatos estructurados desde documentos administrativos municipales en español.


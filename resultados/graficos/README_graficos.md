# Resultados Visuales del Proyecto

Este documento contiene los **gráficos comparativos generados durante la fase de evaluación del sistema** para las combinaciones OCR + LLM y rendimiento individual de cada motor.

---

## 1. Cantidad de documentos procesados con éxito por modelo LLM

![Documentos exitosos por modelo LLM](./cantidad_documentos_exito_llm.png)

---

## 2. Porcentaje de documentos que contienen clasificadores frecuentes

![Clasificadores frecuentes](./porcentaje_clasificadores_llm.png)

---

## 3. Promedio de clasificadores extraídos por documento (por LLM)

![Promedio de clasificadores](./promedio_llaves_llm.png)

---

## 4. Tiempo promedio de ejecución por modelo LLM

![Tiempo LLM](./tiempo_promedio_ejecucion_llm.png)

---

## 5. Tiempo promedio de ejecución por motor OCR

![Tiempo OCR](./tiempo_promedio_ocr.png)

---

## 6. Tiempo total promedio por combinación OCR + LLM

![Combinaciones OCR + LLM](./tiempo_total_promedio_combinacion.png)

---

## 7. Uso promedio de CPU por motor OCR

![CPU OCR](./uso_promedio_cpu_ocr.png)

---

## 8. Uso promedio de GPU por modelo LLM

![GPU LLM](./uso_promedio_gpu_llm.png)

---

## 9. Uso promedio de VRAM por modelo LLM

![VRAM LLM](./uso_promedio_vram_llm.png)

---

Cada uno de estos gráficos fue generado a partir de un análisis automatizado sobre 9,000 documentos utilizando FastAPI + Ollama, midiendo rendimiento, eficiencia y calidad de extracción de metadatos estructurados.

### resultados/graficos/README\_graficos.md

# Resultados Visuales del Proyecto

Este documento reúne los **gráficos de la fase experimental** donde se evaluaron motores **OCR**, **LLMs** y sus combinaciones, sobre más de **3000 documentos municipales**. Se midieron **tiempos de ejecución**, **uso de recursos** y **calidad de extracción** de clasificadores.

## Índice

1. Arquitectura y síntesis de resultados
2. Métricas de calidad (clasificadores, precisión y similitud)
3. Rendimiento y tiempos
4. Consumo de recursos (CPU/GPU/VRAM)
5. Conclusiones

---

## 1. Arquitectura y síntesis de resultados

* Diagrama de solución:
  ![Diagrama de solución](./diagrama_solucion.png)
* Diagrama de bajo nivel:
  ![Diagrama de bajo nivel](./diagrama_bajo_nivel.png)
* Resumen final:
  ![Resumen final](./resumen_final.png)

---

## 2. Métricas de calidad

**Cobertura y éxito por modelo**

* Documentos procesados con éxito por LLM:
  ![Éxito por LLM](./cantidad_documentos_exito_llm.png)
* Clasificadores frecuentes (porcentaje de documentos con llaves):
  ![Porcentaje clasificadores](./porcentaje_clasificadores_llm.png)
* Promedio de clasificadores por documento (por LLM):
  ![Promedio de llaves por LLM](./promedio_llaves_llm.png)
* Comparación de cantidad de llaves:
  ![Cantidad llaves comparación](./cantidad_llaves_comparacion.png)
* Clasificadores por municipalidad y promedios:
  ![Clasificadores munis](./clasificadores_munis.png)
  ![Promedios clasificadores munis](./promedios_clasificadores_munis.png)

**Calidad de extracción (validación)**

* Precisión exacta:
  ![Precisión exacta](./precision_exacta.png)
* Similitud exacta y fuzzy:
  ![Similitud exacta](./similitud_exacta.png)
  ![Similitud fuzzy](./similitud_fuzzy.png)
* Errores y vacíos detectados:
  ![Errores/ vacíos](./errores_vacios.png)

**Interpretación breve**

* LLaMA 3.2 Municipal y Qwen 2.5 entregan mayor estabilidad en la cantidad de clasificadores y precisión.
* La variabilidad por municipalidad sugiere que **prompting específico por tipo de documento** mejora resultados.

---

## 3. Rendimiento y tiempos

* Tiempo promedio de ejecución por LLM:
  ![Tiempo LLM](./tiempo_promedio_ejecucion_llm.png)
* Tiempo promedio de ejecución por OCR:
  ![Tiempo OCR](./tiempo_promedio_ocr.png)
* Tiempo total promedio por combinación OCR + LLM:
  ![Tiempo combinación](./tiempo_total_promedio_combinacion.png)
* Comparaciones adicionales de tiempo (por PC / global):
  ![Tiempo promedio comparación](./Tiempo_promedio_comparacion.png)
  ![Tiempo LLM por PC](./Tiempo_promedio_llm_pcs.png)
  ![Tiempo total comparación](./tiempo_total_comparacion.png)
  ![Tiempos por documento](./tiempos_pordocumentos.png)
  ![Distribución de tiempos por PC](./distribucion_tiempos_pcs.png)

**Interpretación breve**

* PaddleOCR es consistentemente el **más rápido**.
* Las combinaciones con LLaMA 3.2 y Qwen 2.5 logran **mejor tiempo total** sin sacrificar calidad.

---

## 4. Consumo de recursos

* Uso promedio de CPU por OCR:
  ![CPU OCR](./uso_promedio_cpu_ocr.png)
* Uso promedio de GPU por LLM:
  ![GPU LLM](./uso_promedio_gpu_llm.png)
* Uso promedio de VRAM por LLM:
  ![VRAM LLM](./uso_promedio_vram_llm.png)
* Comparaciones por equipo (GPU/VRAM):
  ![GPU PCs](./gpu_pcs.png)
  ![VRAM PCs](./vram_pcs.png)
  ![Uso GPU comparación](./uso_gpu_comparacion.png)
  ![VRAM comparación](./vram_comparacion.png)
  ![Llaves promedios por PC](./llaves_promedios_pcs.png)

**Interpretación breve**

* El **consumo de VRAM** de LLaMA 3.2 y Qwen 2.5 se mantiene dentro de rangos eficientes para GPUs de rango medio.
* PaddleOCR presenta **bajo uso de CPU** en comparación con alternativas.

---

## 5. Conclusiones

* **OCR ganador**: PaddleOCR (velocidad y estabilidad).
* **LLMs recomendados**: LLaMA 3.2 Municipal (3B) y Qwen 2.5 (3B).
* **Mejor balance global**: combinaciones `paddleocr_llama3` y `paddleocr_qwen`.
* El enfoque con **prompts bien diseñados** resulta **más flexible y replicable** que el fine-tuning por departamento, manteniendo eficiencia y trazabilidad.
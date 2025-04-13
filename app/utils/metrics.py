# utils/metrics.py

import time
import psutil
import GPUtil
from contextlib import contextmanager

@contextmanager
def medir_uso_recursos():
    proceso = psutil.Process()
    inicio = time.time()

    mem_inicio = proceso.memory_info().rss
    cpu_inicio = proceso.cpu_percent(interval=None)

    gpus = GPUtil.getGPUs()
    gpu_info_inicio = {
        gpu.id: {
            "memoria_usada": gpu.memoryUsed,
            "carga": gpu.load
        } for gpu in gpus
    }

    yield_data = {}
    try:
        yield yield_data
    finally:
        fin = time.time()
        mem_fin = proceso.memory_info().rss
        cpu_fin = proceso.cpu_percent(interval=None)

        gpus_fin = GPUtil.getGPUs()
        gpu_info_fin = {
            gpu.id: {
                "memoria_usada": gpu.memoryUsed,
                "carga": gpu.load
            } for gpu in gpus_fin
        }

        # mide del primer GPU si existe
        gpu_metricas = {}
        if gpus:
            id_primera_gpu = gpus[0].id
            gpu_metricas = {
                "vram_usada_MB": round(gpu_info_fin[id_primera_gpu]["memoria_usada"], 2),
                "uso_gpu": round(gpu_info_fin[id_primera_gpu]["carga"] * 100, 2)
            }

        yield_data.update({
            "tiempo_segundos": round(fin - inicio, 4),
            "ram_usada_MB": round((mem_fin - mem_inicio) / (1024 * 1024), 2),
            "cpu_percent": round(cpu_fin, 2),
            **gpu_metricas
        })


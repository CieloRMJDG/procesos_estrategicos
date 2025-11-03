import csv
import os
from datetime import datetime


def generar_reporte(tareas, ruta_salida='data/reporte_tareas.csv'):
    """
    Genera un archivo CSV con la lista de tareas.

    Args:
        tareas: lista de objetos Tarea (de `modules.tareas`).
        ruta_salida: ruta del archivo CSV a escribir (por defecto 'data/reporte_tareas.csv').

    Retorna:
        (exito: bool, mensaje: str)
    """
    try:
        # Asegurar carpeta de salida
        carpeta = os.path.dirname(ruta_salida) or '.'
        os.makedirs(carpeta, exist_ok=True)

        campos = [
            'titulo',
            'descripcion',
            'fecha_vencimiento',
            'completada',
            'fecha_creacion',
            'usuario_asignado'
        ]

        with open(ruta_salida, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=campos)
            writer.writeheader()

            for t in tareas:
                # fecha_creacion puede ser datetime
                fecha_creacion = t.fecha_creacion.isoformat() if isinstance(t.fecha_creacion, datetime) else str(t.fecha_creacion)
                writer.writerow({
                    'titulo': t.titulo,
                    'descripcion': t.descripcion,
                    'fecha_vencimiento': t.fecha_vencimiento,
                    'completada': str(t.completada),
                    'fecha_creacion': fecha_creacion,
                    'usuario_asignado': t.usuario_asignado or ''
                })

        return True, f'Reporte generado en {ruta_salida}'
    except Exception as e:
        return False, f'Error al generar el reporte: {e}'


from datetime import datetime

class Tarea:
    def __init__(self, titulo, descripcion, fecha_vencimiento):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.completada = False

    def marcar_como_completada(self):
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"Tarea: {self.titulo}\nDescripción: {self.descripcion}\nFecha de Vencimiento: {self.fecha_vencimiento}\nEstado: {estado}"
from datetime import datetime

class Tarea:
    """Clase que representa una tarea."""
    def __init__(self, titulo, descripcion, fecha_vencimiento):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.completada = False
        self.fecha_creacion = datetime.now()
        self.usuario_asignado = None

    def marcar_como_completada(self):
        self.completada = True

    def asignar_usuario(self, usuario):
        self.usuario_asignado = usuario
    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"Tarea: {self.titulo}\nDescripción: {self.descripcion}\nFecha de Vencimiento: {self.fecha_vencimiento}\nEstado: {estado}\nFecha de Creación: {self.fecha_creacion}\nUsuario Asignado: {self.usuario_asignado}"

class GestorTareas:
    """Clase para gestionar la lista de tareas."""
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, tarea):
        self.tareas.remove(tarea)

    def listar_tareas(self):
        return self.tareas
    def buscar_tareas_por_usuario(self, usuario):
        return [tarea for tarea in self.tareas if tarea.usuario_asignado == usuario]
    def listar_tareas_pendientes(self):
        return [tarea for tarea in self.tareas if not tarea.completada]
    def listar_tareas_completadas(self):
        return [tarea for tarea in self.tareas if tarea.completada]
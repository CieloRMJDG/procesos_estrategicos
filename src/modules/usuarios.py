import json

class Usuario:
    def __init__(self, nombre: str, contraseña: str, es_jefe: bool):
        self.nombre = nombre
        self.contraseña = contraseña
        self.es_jefe = es_jefe

class SistemaUsuarios:
    def __init__(self):
        self.usuarios = {}
        self.usuario_actual = None
        
        try:
            with open('usuarios.txt', 'r') as archivo:
                for linea in archivo:
                    nombre, contraseña, es_jefe = linea.strip().split(',')
                    es_jefe = es_jefe == 'True'
                    self.usuarios[nombre] = Usuario(nombre, contraseña, es_jefe)
        except:
            print("Iniciando con lista de usuarios vacía")

    def guardar_usuarios(self):
        try:
            with open('usuarios.txt', 'w') as archivo:
                for usuario in self.usuarios.values():
                    archivo.write(f"{usuario.nombre},{usuario.contraseña},{usuario.es_jefe}\n")
        except:
            print("Error al guardar usuarios")

    def registrar_usuario(self, nombre: str, contraseña: str, es_jefe: bool) -> bool:
        if nombre in self.usuarios:
            return False
        
        nuevo_usuario = Usuario(nombre, contraseña, es_jefe)
        self.usuarios[nombre] = nuevo_usuario
        self.guardar_usuarios()
        return True

    def iniciar_sesion(self, nombre: str, contraseña: str) -> bool:
        if nombre in self.usuarios:
            usuario = self.usuarios[nombre]
            if usuario.contraseña == contraseña:
                self.usuario_actual = usuario
                return True
        return False

    def obtener_tipo_usuario(self) -> str:
        if self.usuario_actual:
            return "jefe" if self.usuario_actual.es_jefe else "empleado"
        return None

    def obtener_nombre_usuario(self) -> str:
        if self.usuario_actual:
            return self.usuario_actual.nombre
        return None

    def cerrar_sesion(self):
        self.usuario_actual = None
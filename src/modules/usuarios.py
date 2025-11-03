import json
import os

class Usuario:
    """
    Modelo de Usuario con nombre, contraseña y rol.
    Laura - Gestión de usuarios y manejo de roles
    """
    def __init__(self, nombre: str, contraseña: str, rol: str):
        self.nombre = nombre
        self.contraseña = contraseña
        self.rol = rol  
    
    def es_jefe(self) -> bool:
        """Verifica si el usuario es jefe"""
        return self.rol.lower() == "jefe"
    
    def es_empleado(self) -> bool:
        """Verifica si el usuario es empleado"""
        return self.rol.lower() == "empleado"
    
    def to_dict(self) -> dict:
        """Convierte el usuario a diccionario para guardar en JSON"""
        return {
            "password": self.contraseña,
            "rol": self.rol
        }
    
    def __str__(self):
        return f"Usuario: {self.nombre} - Rol: {self.rol}"

class SistemaUsuarios:
    """
    Sistema de gestión de usuarios con autenticación y roles.
    Laura - Permite registro solo por jefes, carga desde JSON
    """
    def __init__(self, archivo_json='data/usuarios.json'):
        self.archivo_json = archivo_json
        self.usuarios = {}
        self.usuario_actual = None
        self.cargar_usuarios()  
    
    def cargar_usuarios(self):
        """Carga usuarios desde el archivo JSON"""
        try:
            if os.path.exists(self.archivo_json):
                with open(self.archivo_json, 'r', encoding='utf-8') as archivo:
                    datos = json.load(archivo)
                    for nombre, info in datos.items():
                        self.usuarios[nombre] = Usuario(
                            nombre=nombre,
                            contraseña=info['password'],
                            rol=info['rol']
                        )
                print(f"✓ {len(self.usuarios)} usuarios cargados correctamente")
            else:
                print("⚠ Archivo de usuarios no encontrado. Iniciando con lista vacía.")
        except json.JSONDecodeError:
            print("✗ Error al leer el archivo JSON. Iniciando con lista vacía.")
        except Exception as e:
            print(f"✗ Error inesperado al cargar usuarios: {e}")

    def guardar_usuarios(self):
        """Guarda todos los usuarios en el archivo JSON"""
        try:
            os.makedirs(os.path.dirname(self.archivo_json), exist_ok=True)
            
            datos = {}
            for nombre, usuario in self.usuarios.items():
                datos[nombre] = usuario.to_dict()
            
            with open(self.archivo_json, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
            
            print("✓ Usuarios guardados correctamente")
            return True
        except Exception as e:
            print(f"✗ Error al guardar usuarios: {e}")
            return False

    def validar_nombre_usuario(self, nombre: str) -> tuple[bool, str]:
        """
        Valida que el nombre de usuario cumpla con los requisitos.
        Retorna (es_valido, mensaje_error)
        """
        if not nombre or len(nombre.strip()) == 0:
            return False, "El nombre de usuario no puede estar vacío"
        
        if len(nombre) < 3:
            return False, "El nombre debe tener al menos 3 caracteres"
        
        if len(nombre) > 20:
            return False, "El nombre no puede tener más de 20 caracteres"
        
        if not nombre.replace('_', '').replace('-', '').isalnum():
            return False, "El nombre solo puede contener letras, números, guiones y guiones bajos"
        
        return True, ""

    def validar_contraseña(self, contraseña: str) -> tuple[bool, str]:
        """
        Valida que la contraseña cumpla con los requisitos mínimos.
        Retorna (es_valida, mensaje_error)
        """
        if not contraseña or len(contraseña.strip()) == 0:
            return False, "La contraseña no puede estar vacía"
        
        if len(contraseña) < 4:
            return False, "La contraseña debe tener al menos 4 caracteres"
        
        return True, ""

    def validar_rol(self, rol: str) -> tuple[bool, str]:
        """
        Valida que el rol sea válido (jefe o empleado).
        Retorna (es_valido, mensaje_error)
        """
        roles_validos = ["jefe", "empleado"]
        if rol.lower() not in roles_validos:
            return False, f"El rol debe ser 'jefe' o 'empleado'"
        
        return True, ""

    def registrar_usuario(self, nombre: str, contraseña: str, rol: str, registrado_por=None) -> tuple[bool, str]:
        """
        Registra un nuevo usuario en el sistema.
        Solo los jefes pueden registrar nuevos usuarios.
        
        Args:
            nombre: Nombre de usuario
            contraseña: Contraseña del usuario
            rol: Rol del usuario ("jefe" o "empleado")
            registrado_por: Usuario que está registrando (debe ser jefe)
        
        Returns:
            (exito, mensaje)
        """
        if registrado_por and not registrado_por.es_jefe():
            return False, "✗ Solo los jefes pueden registrar nuevos usuarios"
        
        # aca se valida nombre de usuario
        valido, mensaje = self.validar_nombre_usuario(nombre)
        if not valido:
            return False, f"✗ {mensaje}"
        
        # aca se verifica si el usuario ya existe
        if nombre in self.usuarios:
            return False, f"✗ El usuario '{nombre}' ya existe"
        
        # se confirma la contraseñs
        valido, mensaje = self.validar_contraseña(contraseña)
        if not valido:
            return False, f"✗ {mensaje}"
        
        # se valida el rol
        valido, mensaje = self.validar_rol(rol)
        if not valido:
            return False, f"✗ {mensaje}"
        
        # se crea y se guarda el nuevo usuario
        nuevo_usuario = Usuario(nombre, contraseña, rol.lower())
        self.usuarios[nombre] = nuevo_usuario
        
        if self.guardar_usuarios():
            return True, f"✓ Usuario '{nombre}' registrado exitosamente como {rol}"
        else:
            # si llega a fallar el guardado, se revierte
            del self.usuarios[nombre]
            return False, "✗ Error al guardar el usuario"

    def iniciar_sesion(self, nombre: str, contraseña: str) -> tuple[bool, str]:
        """
        Inicia sesión con un usuario existente.
        Retorna (exito, mensaje)
        """
        if not nombre or not contraseña:
            return False, "✗ Nombre de usuario y contraseña son requeridos"
        
        if nombre not in self.usuarios:
            return False, "✗ Usuario o contraseña incorrectos"
        
        usuario = self.usuarios[nombre]
        if usuario.contraseña != contraseña:
            return False, "✗ Usuario o contraseña incorrectos"
        
        self.usuario_actual = usuario
        return True, f"✓ Bienvenido {nombre}!"

    def cerrar_sesion(self):
        """Cierra la sesión del usuario actual"""
        if self.usuario_actual:
            nombre = self.usuario_actual.nombre
            self.usuario_actual = None
            return True, f"✓ Sesión cerrada. ¡Hasta luego {nombre}!"
        return False, "✗ No hay ninguna sesión activa"

    def obtener_usuario_actual(self) -> Usuario:
        """Retorna el usuario actualmente autenticado"""
        return self.usuario_actual

    def obtener_tipo_usuario(self) -> str:
        """Retorna el tipo de usuario actual (jefe/empleado)"""
        if self.usuario_actual:
            return self.usuario_actual.rol
        return None

    def obtener_nombre_usuario(self) -> str:
        """Retorna el nombre del usuario actual"""
        if self.usuario_actual:
            return self.usuario_actual.nombre
        return None
    
    def listar_usuarios(self) -> list:
        """Retorna lista de todos los usuarios"""
        return list(self.usuarios.values())
    
    def listar_empleados(self) -> list:
        """Retorna lista de usuarios con rol empleado"""
        return [u for u in self.usuarios.values() if u.es_empleado()]
    
    def listar_jefes(self) -> list:
        """Retorna lista de usuarios con rol jefe"""
        return [u for u in self.usuarios.values() if u.es_jefe()]
    
    def buscar_usuario(self, nombre: str) -> Usuario:
        """Busca y retorna un usuario por nombre"""
        return self.usuarios.get(nombre)
    
    def existe_usuario(self, nombre: str) -> bool:
        """Verifica si existe un usuario con ese nombre"""
        return nombre in self.usuarios

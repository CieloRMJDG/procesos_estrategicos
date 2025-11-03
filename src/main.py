
from modules.usuarios import SistemaUsuarios
from modules.tareas import Tarea, GestorTareas #Importar clases Tarea y GestorTareas, para usar a futuro


def mostrar_menu_principal():
    print("\n=== Sistema de Tareas ===")
    print("1. Entrar al sistema")
    print("2. Crear nuevo usuario")
    print("3. Salir")
    return input("¿Qué quieres hacer? ")

def mostrar_menu_usuario(es_jefe):
    print("\n=== Menú de Usuario ===")
    if es_jefe:
        print("1. Ver todos los empleados")
        print("2. Ver todas las tareas")
        print("3. Crear tarea nueva")
    else:
        print("1. Ver mis tareas")
        print("2. Crear tarea nueva")
    print("3. Salir")
    return input("¿Qué quieres hacer? ")

def main():
    sistema = SistemaUsuarios()
    while True:
        opcion = mostrar_menu_principal()
        if opcion == "1":
            nombre = input("Nombre de usuario: ")
            contraseña = input("Contraseña: ")
            if sistema.iniciar_sesion(nombre, contraseña):
                print(f"¡Bienvenido {nombre}!")
                while True:
                    es_jefe = sistema.obtener_tipo_usuario() == "jefe"
                    opcion = mostrar_menu_usuario(es_jefe)
                    if opcion == "3":
                        sistema.cerrar_sesion()
                        print("¡Hasta luego!")
                        break
                    else:
                        print("Esa función todavía no está lista")
            else:
                print("Usuario o contraseña incorrectos")
        elif opcion == "2":
            nombre = input("Elige un nombre de usuario: ")
            contraseña = input("Elige una contraseña: ")
            respuesta = input("¿Será jefe? (si/no): ").lower()
            es_jefe = respuesta == "si"
            if sistema.registrar_usuario(nombre, contraseña, es_jefe):
                print("¡Usuario creado!")
            else:
                print("Ese nombre ya existe, elige otro")
        elif opcion == "3":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción no válida, intenta de nuevo")

if __name__ == "__main__":
    main()

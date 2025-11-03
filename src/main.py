from modules.usuarios import SistemaUsuarios
from modules.tareas import Tarea, GestorTareas # Importar clases Tarea y GestorTareas, para usar a futuro


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
        print("4. Salir")
    else:
        print("1. Ver mis tareas")
        print("2. Crear tarea nueva")
        print("3. Salir")
    return input("¿Qué quieres hacer? ")

def main():
    sistema = SistemaUsuarios()
    gestor = GestorTareas()
    while True:
        opcion = mostrar_menu_principal()
        if opcion == "1":
            nombre = input("Nombre de usuario: ")
            contraseña = input("Contraseña: ")
            exito, msg = sistema.iniciar_sesion(nombre, contraseña)
            if exito:
                print(msg)
                # Menú del usuario autenticado
                while True:
                    es_jefe = sistema.obtener_tipo_usuario() == "jefe"
                    opcion = mostrar_menu_usuario(es_jefe)
                    if (es_jefe and opcion == "4") or (not es_jefe and opcion == "3"):
                        sistema.cerrar_sesion()
                        print("¡Hasta luego!")
                        break
                    # Opciones para jefe
                    if es_jefe:
                        if opcion == "1":
                            empleados = sistema.listar_empleados()
                            if not empleados:
                                print("No hay empleados registrados.")
                            else:
                                print("\n-- Empleados --")
                                for e in empleados:
                                    print(f"- {e.nombre} (rol: {e.rol})")
                        elif opcion == "2":
                            tareas = gestor.listar_tareas()
                            if not tareas:
                                print("No hay tareas registradas.")
                            else:
                                print("\n-- Todas las tareas --")
                                for t in tareas:
                                    print(t)
                                    print("-------------------")
                        elif opcion == "3":
                            titulo = input("Título de la tarea: ")
                            descripcion = input("Descripción: ")
                            fecha = input("Fecha de vencimiento (texto): ")
                            asignar = input("¿Asignar a un usuario ahora? (si/no): ").lower()
                            tarea = Tarea(titulo, descripcion, fecha)
                            if asignar == "si":
                                usuario_asig = input("Nombre de usuario a asignar: ")
                                usuario_obj = sistema.buscar_usuario(usuario_asig)
                                if usuario_obj:
                                    tarea.asignar_usuario(usuario_asig)
                                    print(f"Tarea asignada a {usuario_asig}")
                                else:
                                    print("Usuario no encontrado. La tarea quedará sin asignar.")
                            gestor.agregar_tarea(tarea)
                            print("Tarea creada correctamente.")
                        else:
                            print("Opción no válida, intenta de nuevo")
                    # Opciones para empleado
                    else:
                        usuario_actual = sistema.obtener_nombre_usuario()
                        if opcion == "1":
                            tareas_usuario = gestor.buscar_tareas_por_usuario(usuario_actual)
                            if not tareas_usuario:
                                print("No tienes tareas asignadas.")
                            else:
                                print(f"\n-- Tareas de {usuario_actual} --")
                                for t in tareas_usuario:
                                    print(t)
                                    print("-------------------")
                        elif opcion == "2":
                            titulo = input("Título de la tarea: ")
                            descripcion = input("Descripción: ")
                            fecha = input("Fecha de vencimiento (texto): ")
                            tarea = Tarea(titulo, descripcion, fecha)
                            tarea.asignar_usuario(usuario_actual)
                            gestor.agregar_tarea(tarea)
                            print("Tarea creada y asignada a ti.")
                        else:
                            print("Opción no válida, intenta de nuevo")
            else:
                # iniciar_sesion devuelve (False, mensaje) en caso de fallo
                print(msg)
        elif opcion == "2":
            nombre = input("Elige un nombre de usuario: ")
            contraseña = input("Elige una contraseña: ")
            respuesta = input("¿Será jefe? (si/no): ").lower()
            rol = "jefe" if respuesta == "si" else "empleado"
            exito, msg = sistema.registrar_usuario(nombre, contraseña, rol)
            if exito:
                print(msg)
            else:
                print(msg)
        elif opcion == "3":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción no válida, intenta de nuevo")

if __name__ == "__main__":
    main()

# Sistema de Gestión de Tareas con Roles (Jefe/Empleado)

---

**INSTITUCIÓN:** Servicio Nacional de Aprendizaje – SENA / Centro de Biotecnología  
**PROGRAMA:** Análisis y Desarrollo de Software  
**APRENDICES:** Juan José Bocanegra, Cielo Rodriguez , Jeonardo Perche y Laura Fonseca  
**INSTRUCTOR:** Esteban Hernández  
**FICHA:** 3203082  

---

## ¿Qué hace el sistema?

- Inicio de sesión por usuario (autenticación)
- Roles: Jefe / Empleado
- El jefe puede crear y asignar tareas a un empleado
- Cada usuario tiene sus propias tareas guardadas
- Se puede generar reporte CSV con las tareas y su estado

---

## Distribución del Trabajo

### CIELO - Autenticación
Encargada de desarrollar el sistema de autenticación del programa. Implementa el inicio de sesión, valida credenciales de usuario y hace la lectura de información desde el archivo usuarios.json. Luego de iniciar sesión, identifica correctamente el rol del usuario (jefe o empleado).

**Entrega:** Módulo integrado en `usuarios.py`

### LAURA - Gestión de Usuarios y Roles
Encargada de la gestión de usuarios y el manejo de roles dentro del sistema. Define la estructura del modelo User con atributos como nombre de usuario, contraseña y rol. Responsable de permitir el registro de nuevos usuarios desde el rol jefe.

**Entrega:** Módulo `usuarios.py` con clase Usuario y SistemaUsuarios, asegurando la correcta carga, almacenamiento y validación de usuarios.

### JEONARDO - Módulo de Tareas
Responsable del módulo de tareas. Crea la estructura de la clase Task e implementa acciones como crear tareas nuevas, asignarlas a usuarios, mostrarlas en la consola y actualizar su estado (pendiente o completada). Gestiona el archivo `tareas.csv` manteniendo las tareas guardadas correctamente.

**Entrega:** Módulo `tareas.py` integrado al menú principal

### BOCANEGRA - Interfaz y Reportes
A cargo del menú de interacción con el usuario desde consola. Presenta opciones según el rol del usuario, permite el acceso a las funciones de usuarios y tareas, maneja errores e información visual. Responsable del módulo de reportes, generando un archivo CSV con las tareas registradas.

**Entrega:** `main.py` y `reporte.py`, asegurando una experiencia clara y funcional

---

## Sistema de línea de comandos en Python que permite:

1. **Autenticación por usuario** - Cada persona inicia sesión con sus credenciales
2. **Roles diferenciados** - Funciones específicas para jefes y empleados
3. **Gestión de tareas** - Crear, asignar, visualizar y actualizar estado
4. **Persistencia de datos** - Usuarios en JSON, tareas en CSV
5. **Reportes automáticos** - Exportación de tareas a CSV

---

## Arquitectura del Sistema
```
Sistema de Tareas
│
├── Módulo de Usuarios (usuarios.py)
│   ├── Clase Usuario
│   ├── Clase SistemaUsuarios
│   └── Validaciones y autenticación
│
├── Módulo de Tareas (tareas.py)
│   ├── Clase Tarea
│   ├── Gestión de tareas (crear, asignar, actualizar)
│   └── Lectura/escritura de CSV
│
├── Módulo de Reportes (reporte.py)
│   └── Generación de CSV con todas las tareas
│
└── Interfaz Principal (main.py)
    ├── Menú de inicio
    ├── Menú de jefe
    └── Menú de empleado
```

---

## Estructura del Proyecto
```
/procesosestrategicosmain
├── data/
│   └── usuarios.json        # Base de datos de usuarios
├── src/
│   ├── main.py              # Punto de entrada y menú principal (Bocanegra)
│   ├── modules/
│   │   ├── __init__.py      # Inicialización del paquete
│   │   ├── usuarios.py      # Gestión de usuarios y roles (Laura)
│   │   ├── cargar.py        # Carga de datos (Cielo)
│   │   ├── tareas.py        # Gestión de tareas (Leonardo)
│   │   └── reporte.py       # Generación de reportes CSV (Bocanegra)
│   └── data/
│       └── tareas.csv       # Almacenamiento de tareas
├── README.md
├── .gitignore
└── usuarios.txt             
```

---

## Requisitos

- Python 3.11 o superior
- No requiere librerías externas (solo módulos estándar de Python)

---

## Instalación y Uso

### 1. Clonar el repositorio
```bash
< git clone https://github.com/CieloRMJDG/procesos_estrategicos.git
```

### 2. Crear entorno virtual (opcional)
```bash
# Windows
python -m py_compile .\src\main.py 

# macOS/Linux
python3 -m py_compile ./src/main.py
```

### 3. Ejecutar el programa
```bash
 .\src\main.py 
```

---

## Ejemplos de Uso

### Iniciar sesión
```
=== Sistema de Tareas ===
1. Entrar al sistema
2. Crear nuevo usuario
3. Salir
¿Qué quieres hacer? 1

Nombre de usuario: admin
Contraseña: admin123

Bienvenido admin!
```

### Menú de Jefe
```
=== Menú de Usuario ===
1. Ver todos los empleados
2. Ver todas las tareas
3. Crear tarea nueva
4. Salir
```

### Menú de Empleado
```
=== Menú de Usuario ===
1. Ver mis tareas
2. Actualizar estado de tarea
3. Generar reporte
4. Salir
```

---

## Temas de Python Aplicados

- **POO (Programación Orientada a Objetos)** - Clases Usuario, Tarea
- **Manejo de archivos** - Lectura/escritura JSON y CSV
- **Diccionarios y listas** - Almacenamiento de datos
- **Funciones y módulos** - Organización del código
- **Excepciones** - Try/except para manejo de errores
- **Validaciones** - Control de datos de entrada
- **Type hints** - Tipado de variables
- **List comprehensions** - Filtrado de datos
- **Control de flujo** - If/elif/else, while, for
- **Strings y formato** - f-strings, métodos de string

---

## Estado del Proyecto

### Completado 
- Módulo de usuarios (Laura)
- Sistema de autenticación (Cielo)
- Estructura del proyecto

### En Desarrollo
- Módulo de tareas (Leonardo)
- Interfaz de menús (Bocanegra)
- Generación de reportes (Bocanegra)

---

## Commits por Integrante

Cada integrante del equipo ha realizado al menos 3 commits significativos:

- **Cielo:** Sistema de autenticación y validación de credenciales
- **Laura:** Clase Usuario, SistemaUsuarios, validaciones robustas
- **Jeonardo:** Clase Tarea, gestión de tareas, manejo de CSV
- **Bocanegra:** Menús interactivos, reportes CSV, experiencia de usuario

---

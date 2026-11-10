# GESTOR DE TAREAS

Autor: Liliana Chávez Pérez

## 1. Descripción del proyecto

El Gestor de Tareas es un programa desarrollado en Python que permite
administrar las actividades pendientes de un equipo de trabajo.

El programa funciona desde la consola y utiliza Programación
Orientada a Objetos (POO) para organizar el código.

## 2. Lenguaje y herramientas utilizadas

- **Lenguaje:** Python 3.
- **Paradigma:** Programación Orientada a Objetos (POO).
- **Editor de código:** Visual Studio Code.
- **Almacenamiento:** Lista en memoria.

## 3. Estructura del proyecto

El código está organizado en cuatro bloques principales:

### Bloque 1. Clase Tarea

Se encarga de crear y almacenar la información de cada tarea.

Sus atributos son:

- **id**: identificador único.
- **titulo**: nombre o descripción de la tarea.
- **prioridad**: nivel de importancia (alta, media o baja).
- **completada**: estado de la tarea.

También contiene métodos para cambiar el estado de una tarea
y obtener sus datos.

### Bloque 2. Clase GestorTareas

Administra todas las tareas registradas en el programa.

Sus funciones principales son:

- Registrar nuevas tareas.
- Mostrar todas las tareas en una tabla.
- Buscar tareas mediante su ID.
- Consultar la información de una tarea.
- Marcar tareas como completadas.
- Eliminar tareas registradas.

También realiza las validaciones necesarias para evitar datos
incorrectos.

### Bloque 3. Clase Aplicacion

Controla la interacción con el usuario desde la consola.

Se encarga de:

- Mostrar el menú principal.
- Solicitar los datos de las tareas.
- Leer y validar el ID ingresado.
- Ejecutar la opción seleccionada.
- Mantener el programa activo hasta que el usuario decida salir.

### Bloque 4. Punto de inicio

Es el bloque que permite iniciar el programa.

Crea un objeto de la clase **Aplicacion** y ejecuta el método
**iniciar()**, que pone en marcha el menú principal.

## 4. Funcionalidades implementadas

El programa cuenta con las siguientes opciones:

1 Agregar tarea: Registra una tarea con título y prioridad.
2 Mostrar tareas: Presenta las tareas registradas en una tabla.
3 Buscar tarea: Consulta una tarea mediante su ID.
4 Completar tarea: Cambia el estado de pendiente a completada.
5 Eliminar tarea: Elimina una tarea mediante su ID.
6 Salir: Finaliza la ejecución del programa.

## 5. Validaciones implementadas

Para asegurar el correcto funcionamiento del programa se
implementaron las siguientes validaciones:

- El título de una tarea no puede estar vacío.
- La prioridad solo acepta los valores alta, media o baja.
- Cada tarea recibe un ID único generado automáticamente.
- El ID debe ser un número entero mayor que cero.
- Si se busca un ID que no existe, se informa al usuario.
- No se permite completar una tarea que ya está completada.
- No se permite eliminar una tarea que no existe.
- Si no hay tareas registradas, se muestra un mensaje informativo.
- Si el usuario selecciona una opción incorrecta, el programa
  muestra un mensaje de error.

## 6. Presentación de las tareas

La opción de mostrar tareas utiliza una tabla en la consola
para organizar la información.
La tabla contiene cuatro columnas:

- ID.
- Título.
- Prioridad.
- Estado.

También se muestra el total de tareas existentes.

## 7. Almacenamiento de datos

Las tareas se almacenan en una lista de Python dentro de la
clase **GestorTareas**.

Los datos se mantienen mientras el programa está en
ejecución. Al cerrar el programa, las tareas registradas se pierden.

## 8. Instrucciones de ejecución

Para ejecutar el programa se deben seguir estos pasos:

1. Instalar Python 3 en el equipo.
2. Abrir Visual Studio Code.
3. Crear o abrir la carpeta del proyecto.
4. Guardar el código fuente con el nombre **gestor_tareas.py**.
5. Abrir una terminal dentro de la carpeta.
6. Ejecutar el siguiente comando: gestor_tareas.py
7. Una vez iniciado, aparecerá el menú principal en la consola.
8. Seleccionar la opción deseada e ingresar los datos solicitados.

## 9. Recursos y herramientas de apoyo

Para el desarrollo de esta solución se utilizaron los siguientes
recursos:

- Python 3 para la programación del sistema.
- Visual Studio Code como entorno de desarrollo.
- Documentación de Python como material de consulta.
- ChatGPT como herramienta de apoyo (errores y estructuras)

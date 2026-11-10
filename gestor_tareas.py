# ********************GESTOR DE TAREAS************************

# BLOQUE 1. CLASE TAREA
# ============================================================

class Tarea:
    # Guarda los datos de una tarea.

    def __init__(self, id_tarea, titulo, prioridad):
        self.id = id_tarea
        self.titulo = titulo
        self.prioridad = prioridad
        self.completada = False

    def marcar_como_completada(self):
        # Cambia el estado de la tarea a completada.
        self.completada = True

    def mostrar(self):
        # Muestra los datos de la tarea.

        estado = "Completada" if self.completada else "Pendiente"

        return [
            self.id,
            self.titulo,
            self.prioridad.capitalize(),
            estado
        ]

# BLOQUE 2. CLASE GESTOR DE TAREAS
# ============================================================

class GestorTareas:
    # Administra la lista de tareas.

    def __init__(self):
        self.tareas = []
        self.siguiente_id = 1
        self.prioridades = ("alta", "media", "baja")

    def registrar_tarea(self, titulo, prioridad):
        # Crea una tarea si los datos son validos.

        titulo = titulo.strip()
        prioridad = prioridad.strip().lower()

        # Validar que el titulo no este vacio.
        if not titulo:
            print("\nError: el titulo no puede estar vacio.")
            return

        # Validar que la prioridad sea correcta.
        if prioridad not in self.prioridades:
            print("\nError: usa alta, media o baja.")
            return

        # Crear y guardar la nueva tarea.
        nueva = Tarea(self.siguiente_id, titulo, prioridad) # objeto, clase del bloque 1
        self.tareas.append(nueva)
        self.siguiente_id += 1

        print(f"\nTarea registrada. ID asignado: {nueva.id}")

    def mostrar_tareas(self):
        # Muestra todas las tareas en una tabla.

        if not self.tareas:
            print("\nNo hay tareas registradas.")
            return

        # Encabezados de la tabla.
        encabezados = ["ID", "TITULO", "PRIORIDAD", "ESTADO"]

        # Obtener los datos de cada tarea.
        filas = [tarea.mostrar() for tarea in self.tareas]

        # Calcular el ancho de cada columna.
        anchos = []

        for i, encabezado in enumerate(encabezados):
            ancho = max(
                len(str(fila[i])) for fila in filas
            )
            anchos.append(max(len(encabezado), ancho) + 2)

        # Crear la linea que separa las columnas.
        separador = "+".join(
            "-" * ancho for ancho in anchos
        )

        # Mostrar titulo.
        print("\n" + "=" * len(separador))
        print("                 LISTA DE TAREAS")
        print("=" * len(separador))

        # Mostrar encabezados.
        print(separador)
        print("|".join(
            encabezado.center(anchos[i])
            for i, encabezado in enumerate(encabezados)
        ))
        print(separador)

        # Mostrar las tareas.
        for fila in filas:
            print("|".join(
                str(fila[i]).ljust(anchos[i])
                for i in range(len(fila))
            ))

        print(separador)
        print(f"Total de tareas: {len(self.tareas)}")

    def buscar_por_id(self, id_tarea):
        # Busca una tarea por su ID y la retorna si existe.

        for tarea in self.tareas:
            if tarea.id == id_tarea:
                return tarea

        return None

    def consultar_tarea(self, id_tarea):
        # Busca y muestra una tarea.

        tarea = self.buscar_por_id(id_tarea)

        if tarea is None:
            print(f"\nNo existe una tarea con el ID {id_tarea}.")
            return

        print("\n===== TAREA ENCONTRADA =====")
        datos = tarea.mostrar()

        print(f"ID:        {datos[0]}")
        print(f"TITULO:    {datos[1]}")
        print(f"PRIORIDAD: {datos[2]}")
        print(f"ESTADO:    {datos[3]}")

    def completar_tarea(self, id_tarea):
        # Marca una tarea pendiente como completada.

        tarea = self.buscar_por_id(id_tarea)

        if tarea is None:
            print(f"\nNo existe una tarea con el ID {id_tarea}.")
            return

        if tarea.completada:
            print("\nLa tarea ya estaba completada.")
            return

        tarea.marcar_como_completada()
        print("\nTarea marcada como completada.")

    def eliminar_tarea(self, id_tarea):
        # Borra una tarea usando su ID.

        tarea = self.buscar_por_id(id_tarea)

        if tarea is None:
            print(f"\nNo existe una tarea con el ID {id_tarea}.")
            return

        self.tareas.remove(tarea)
        print("\nTarea eliminada de forma correcta.")

# BLOQUE 3. CLASE DE LA APLICACION
# ============================================================

class Aplicacion:
    # Controla el menu y la entrada de datos.

    def __init__(self):
        self.gestor = GestorTareas()
        self.activa = True

    def mostrar_menu(self):
        # Imprime las opciones del programa.

        print("\n========== GESTOR DE TAREAS ==========")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Buscar tarea")
        print("4. Completar tarea")
        print("5. Eliminar tarea")
        print("6. Salir")
        print("=" * 38)

    def pedir_id(self):
        # Pide un ID y valida que sea un numero entero positivo.

        dato = input("ID de la tarea: ").strip()

        try:
            id_tarea = int(dato)

            if id_tarea <= 0:
                print("\nError: el ID debe ser mayor que cero.")
                return None

            return id_tarea

        except ValueError:
            print("\nError: escribe un numero entero.")
            return None

    def agregar(self):
        # Pide los datos para crear una tarea.

        print("\n===== AGREGAR TAREA =====")

        titulo = input("Titulo: ")
        prioridad = input("Prioridad (alta, media o baja): ")

        self.gestor.registrar_tarea(titulo, prioridad)

    def buscar(self):
        # Pide el ID y consulta la tarea.

        print("\n===== BUSCAR TAREA =====")

        id_tarea = self.pedir_id()

        if id_tarea is not None:
            self.gestor.consultar_tarea(id_tarea)

    def completar(self):
        # Pide el ID y completa la tarea.

        print("\n===== COMPLETAR TAREA =====")

        id_tarea = self.pedir_id()

        if id_tarea is not None:
            self.gestor.completar_tarea(id_tarea)

    def eliminar(self):
        # Pide el ID y elimina la tarea.

        print("\n===== ELIMINAR TAREA =====")

        id_tarea = self.pedir_id()

        if id_tarea is not None:
            self.gestor.eliminar_tarea(id_tarea)

    def ejecutar_opcion(self, opcion):
        # Llama a la accion elegida.

        if opcion == "1":
            self.agregar()

        elif opcion == "2":
            self.gestor.mostrar_tareas()

        elif opcion == "3":
            self.buscar()

        elif opcion == "4":
            self.completar()

        elif opcion == "5":
            self.eliminar()

        elif opcion == "6":
            self.activa = False
            print("\nGracias por usar el Gestor de Tareas.\nAutor: Liliana Chávez Pérez\nPrograma de consola para crear, ver, buscar, completar y borrar tareas de un equipo de trabajo.\n")

        else:
            print("\nOpcion no valida. Elige un numero del 1 al 6.")

    def iniciar(self):
        # Inicia el ciclo principal del programa.

        while self.activa:
            self.mostrar_menu()

            opcion = input("Selecciona una opcion: ").strip()

            self.ejecutar_opcion(opcion)

# ============================================================
# BLOQUE 4. PUNTO DE INICIO
# ============================================================

if __name__ == "__main__":
    app = Aplicacion()
    app.iniciar()
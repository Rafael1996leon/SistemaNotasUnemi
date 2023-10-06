class Nota:
    def __init__(self, id, n1, n2, ex1):
        self.id = id
        self.n1 = n1
        self.n2 = n2
        self.ex1 = ex1

    def calcular_promedio(self):
        return (self.n1 + self.n2 + self.ex1) / 3

    def mostrar_aprobado(self):
        promedio = self.calcular_promedio()
        if promedio >= 3.0:
            return f"Alumno aprobado con un promedio de {promedio}"
        else:
            return f"Alumno reprobado con un promedio de {promedio}"


class Semestre:
    def __init__(self, nivel):
        self.nivel = nivel
        self.lista_asignaturas = []
        self.estudiantes_inscritos = []

    def iniciar_semestre(self):
        self.estudiantes_inscritos = []
        self.lista_asignaturas = []
        print(f"Se ha iniciado el semestre {self.nivel}")

    def inscribir_estudiantes_asignaturas(self):
        estudiante = input("Ingrese el nombre del estudiante: ")
        asignaturas = input(
            "Ingrese las asignaturas a las que desea inscribir al estudiante (separadas por coma): ").split(", ")

        for asignatura in asignaturas:
            if asignatura in self.lista_asignaturas:
                if (estudiante, asignatura) not in self.estudiantes_inscritos:
                    self.estudiantes_inscritos.append((estudiante, asignatura))
                    print(f"{estudiante} se ha inscrito en {asignatura} en el semestre {self.nivel}")
                else:
                    print(f"{estudiante} ya está inscrito en {asignatura} en el semestre {self.nivel}")
            else:
                print(f"{asignatura} no está disponible en el semestre {self.nivel}")

    def registrar_asignaturas(self, asignatura):
        self.lista_asignaturas.append(asignatura)
        print(f"Asignatura {asignatura.nombre} registrada en el semestre {self.nivel}")

    def mostrar_informacion(self):
        print(f"Información del Semestre {self.nivel}:")
        print("Asignaturas planificadas:")
        for asignatura in self.lista_asignaturas:
            print(f"- {asignatura.nombre}")
        print("Estudiantes inscritos:")
        for estudiante, asignatura in self.estudiantes_inscritos:
            print(f"- {estudiante} inscrito en {asignatura}")


class Carrera:
    def __init__(self):
        self.lista_carreras = []

    def agregar_nueva_carrera(self):
        nombre = input("Ingrese el nombre de la carrera: ")
        id_carrera = input("Ingrese el ID de la carrera: ")
        detalle = input("Ingrese el detalle de la carrera: ")
        lista_asignaturas = input("Ingrese las asignaturas de la carrera (separadas por coma): ").split(", ")

        nueva_carrera = {
            "nombre": nombre,
            "id_carrera": id_carrera,
            "detalle": detalle,
            "lista_asignaturas": lista_asignaturas
        }
        self.lista_carreras.append(nueva_carrera)
        print(f"Carrera {nombre} registrada con éxito.")

    def mostrar_carrera(self):
        id_carrera = input("Ingrese el ID de la carrera que desea mostrar: ")
        for carrera in self.lista_carreras:
            if carrera["id_carrera"] == id_carrera:
                print(f"Nombre de la carrera: {carrera['nombre']}")
                print(f"ID de la carrera: {carrera['id_carrera']}")
                print(f"Detalle de la carrera: {carrera['detalle']}")
                print("Asignaturas en la carrera:")
                for asignatura in carrera['lista_asignaturas']:
                    print(f"- {asignatura}")
                return
        print(f"No se encontró una carrera con ID {id_carrera}")


class Asignatura:
    def __init__(self):
        self.lista_asignaturas = []

    def agregar_nueva_asignatura(self):
        nombre = input("Ingrese el nombre de la asignatura: ")
        docente = input("Ingrese el nombre del docente a cargo: ")

        nueva_asignatura = {
            "nombre": nombre,
            "docente": docente
        }
        self.lista_asignaturas.append(nueva_asignatura)
        print(f"Asignatura {nombre} registrada con éxito.")

    def mostrar_asignatura(self):
        nombre = input("Ingrese el nombre de la asignatura que desea mostrar: ")
        for asignatura in self.lista_asignaturas:
            if asignatura["nombre"] == nombre:
                print(f"Nombre de la asignatura: {asignatura['nombre']}")
                print(f"Docente a cargo: {asignatura['docente']}")
                return
        print(f"No se encontró una asignatura con el nombre {nombre}")

    def asignar_docente(self):
        nombre_asignatura = input("Ingrese el nombre de la asignatura a la que desea asignar un docente: ")
        nombre_docente = input("Ingrese el nombre del docente a asignar: ")

        for asignatura in self.lista_asignaturas:
            if asignatura["nombre"] == nombre_asignatura:
                asignatura["docente"] = nombre_docente
                print(f"Docente {nombre_docente} asignado a la asignatura {nombre_asignatura}.")
                return

        print(f"No se encontró una asignatura con el nombre {nombre_asignatura}.")


class Docente:
    def __init__(self):
        self.registro_notas = []

    def ingreso_notas(self):
        estudiante = input("Ingrese el nombre del estudiante: ")
        asignatura = input("Ingrese el nombre de la asignatura: ")

        for registro in self.registro_notas:
            if registro["estudiante"] == estudiante and registro["asignatura"] == asignatura:
                print(f"El estudiante {estudiante} ya tiene notas registradas para la asignatura {asignatura}.")
                return

        n1 = float(input("Ingrese la nota 1: "))
        n2 = float(input("Ingrese la nota 2: "))
        ex1 = float(input("Ingrese la nota del examen 1: "))

        nuevo_registro = {
            "estudiante": estudiante,
            "asignatura": asignatura,
            "n1": n1,
            "n2": n2,
            "ex1": ex1
        }
        self.registro_notas.append(nuevo_registro)
        print(f"Notas registradas para el estudiante {estudiante} en la asignatura {asignatura}.")

    def cambiar_notas(self):
        estudiante = input("Ingrese el nombre del estudiante: ")
        asignatura = input("Ingrese el nombre de la asignatura: ")

        for registro in self.registro_notas:
            if registro["estudiante"] == estudiante and registro["asignatura"] == asignatura:
                print(f"Notas actuales para el estudiante {estudiante} en la asignatura {asignatura}:")
                print(f"Nota 1: {registro['n1']}")
                print(f"Nota 2: {registro['n2']}")
                print(f"Examen 1: {registro['ex1']}")

                n1 = float(input("Ingrese la nueva nota 1: "))
                n2 = float(input("Ingrese la nueva nota 2: "))
                ex1 = float(input("Ingrese la nueva nota del examen 1: "))

                registro["n1"] = n1
                registro["n2"] = n2
                registro["ex1"] = ex1
                print(f"Notas cambiadas para el estudiante {estudiante} en la asignatura {asignatura}.")
                return

        print(f"No se encontró un registro de notas para el estudiante {estudiante} en la asignatura {asignatura}.")


class Estudiante:
    def __init__(self):
        self.lista_estudiantes = []

    def registrar(self):
        nombre = input("Ingrese el nombre del estudiante: ")
        id_estudiante = input("Ingrese el ID del estudiante: ")
        direccion = input("Ingrese la dirección del estudiante: ")
        correo = input("Ingrese el correo electrónico del estudiante: ")

        nuevo_estudiante = {
            "nombre": nombre,
            "id_estudiante": id_estudiante,
            "direccion": direccion,
            "correo": correo
        }
        self.lista_estudiantes.append(nuevo_estudiante)
        print(f"Estudiante {nombre} registrado con éxito.")

    def mostrar_informacion(self):
        id_estudiante = input("Ingrese el ID del estudiante que desea mostrar: ")
        for estudiante in self.lista_estudiantes:
            if estudiante["id_estudiante"] == id_estudiante:
                print(f"Nombre del estudiante: {estudiante['nombre']}")
                print(f"ID del estudiante: {estudiante['id_estudiante']}")
                print(f"Dirección del estudiante: {estudiante['direccion']}")
                print(f"Correo electrónico del estudiante: {estudiante['correo']}")
                return
        print(f"No se encontró un estudiante con ID {id_estudiante}")


if __name__ == "__main__":
    sistema_notas = Nota()
    sistema_semestres = Semestre()
    sistema_carreras = Carrera()
    sistema_asignaturas = Asignatura()
    sistema_docentes = Docente()
    sistema_estudiantes = Estudiante()

    while True:
        print("\nMENU:")
        print("1. Iniciar nuevo semestre")
        print("2. Inscribir estudiantes en asignaturas")
        print("3. Registrar asignatura")
        print("4. Mostrar información del semestre")
        print("5. Agregar nueva carrera")
        print("6. Mostrar información de una carrera")
        print("7. Agregar nueva asignatura")
        print("8. Mostrar información de una asignatura")
        print("9. Ingresar notas")
        print("10. Cambiar notas")
        print("11. Registrar estudiante")
        print("12. Mostrar información de un estudiante")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nivel = input("Ingrese el nivel del nuevo semestre: ")
            sistema_semestres.iniciar_semestre(nivel)
        elif opcion == "2":
            sistema_semestres.inscribir_estudiantes_asignaturas()
        elif opcion == "3":
            nombre_asignatura = input("Ingrese el nombre de la asignatura a registrar: ")
            asignatura = Asignatura()
            asignatura.agregar_nueva_asignatura(nombre_asignatura)
            sistema_semestres.registrar_asignaturas(asignatura)
        elif opcion == "4":
            sistema_semestres.mostrar_informacion()
        elif opcion == "5":
            sistema_carreras.agregar_nueva_carrera()
        elif opcion == "6":
            sistema_carreras.mostrar_carrera()
        elif opcion == "7":
            sistema_asignaturas.agregar_nueva_asignatura()
        elif opcion == "8":
            sistema_asignaturas.mostrar_asignatura()
        elif opcion == "9":
            sistema_docentes.ingreso_notas()
        elif opcion == "10":
            sistema_docentes.cambiar_notas()
        elif opcion == "11":
            sistema_estudiantes.registrar()
        elif opcion == "12":
            sistema_estudiantes.mostrar_informacion()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida del menú.")

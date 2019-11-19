
def Star_Aplication():

        print("*********************************************")
        print("ESCUELA POLITECNICA NACIONAL")
        print("SISTEMA DE ASIGNACION DOCENTES-ALUMNOS")
        print("SELECCIONE EL NUMERO DE LA OPCION A REALIZAR")
        print("1. INGRESE UN DOCENTE")
        print("2. INGRESE UN ALUMNO")
        print("3. CONSULTAR LISTA DE DOCENTES")
        print("4. CONSULTAR LISTA DE ESTUDIANTES")
        print("5. MODIFICAR DOCENTE")
        print("6. MODIFICAR ALUMNO")
        print("7. ELIMINAR DOCENTE")
        print("8. ELIMINAR ALUMNO")
        print("9. TERMINAR PROGRAMA")
        print("*********************************************")

def add_docente():
    nombre = input("Ingrese el nombre del docente: ")
    materia = input("Ingrese la materia impartida por el docente: ")
    telefono = input("Ingrese el numero telefonico del docente: ")

    try:
        path = "./docentes.txt"
        open_file = open(path,mode="a")
        open_file.write(f"{nombre}, ")
        open_file.write(f"{materia}, ")
        open_file.write(f"{telefono}, ")
    except Exception as error:
        print("No se pudo ingresar el docente")

def add_alumno():
    nombre = input("Ingrese el nombre del alumno")
    telefono = input("Ingrese el numero telefonico del alumno")
    ciudad = input("Ingrese la ciudad de nacimiento del Estudiante")










Star_Aplication()
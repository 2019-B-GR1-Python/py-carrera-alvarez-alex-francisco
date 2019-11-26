def add_docente():
    
    print("\n  INGRESE LA INFORMACION DEL DOCENTE\n")
    codigo = input("  Codigo: ")
    nombre = input("  Nombre: ")
    asignatura = input("  Asignatura que dicta: ")
        
    try:
        path = "./docentes.txt"
        archivo_escritura_abierto = open(path,mode="a") 
        archivo_escritura_abierto.writelines([f"{codigo},{nombre},{asignatura}\n"])
        archivo_escritura_abierto.close()
        print("\n INFORMACION INGRESADA CORRECTAMENTE \n")
    except Exception as error:
        print(f"Error en el ingreso: {error}")

def add_student():
    
    print("\n  INGRESE LA INFORMACION DEL ESTUDIANTE\n")
    codigo = input("  Codigo: ")
    nombre = input("  Nombre: ")
    apellido = input("  Apellido: ")
    curso = input("  Curso: ")
        
    try:
        path = "./alumnos.txt"
        archivo_escritura_abierto = open(path,mode="a") 
        archivo_escritura_abierto.writelines([f"{codigo},{nombre},{apellido},{curso}\n"])
        archivo_escritura_abierto.close()
        print("\n INFORMACION INGRESADA CORRECTAMENTE \n")
    except Exception as error:
        print(f"Error en el ingreso: {error}")


def read_docente():
    try:
        path='./docentes.txt'
        archivo_abierto = open(path)
        lineas= archivo_abierto.readlines()
        print("\nDOCENTES\n")
        for linea in lineas:
            print(f"  {linea}")
        archivo_abierto.close
    except Exception as error:
        print(f"ERROR AL CARGAR LOS DOCENTES: {error}")
    
    
def read_student():
    try:
        path='./alumnos.txt'
        archivo_abierto = open(path)
        lineas= archivo_abierto.readlines()
        print("\nESTUDIANTES\n")
        for linea in lineas:
            print(f"  {linea}")
        archivo_abierto.close
    except Exception as error:
        print(f"ERROR AL CARGAR LOS ESTUDIANTES: {error}")
        
        
def modify_docente():
    read_docente()
    codigo = input("\n  INGRESE EL CODIGO DEL DOCENTE A MODIFICAR: ")
    try:
        path="./docentes.txt"
        archivo_abierto = open(path, mode="r+")
        lineas = archivo_abierto.readlines()
        archivo_abierto.seek(0)
        for linea in lineas:
            if codigo in linea:
                nombre = input("  INGRESE EL NOMBRE DEL DOCENTE: ")
                asignatura = input("  INGRESE LA ASIGNATURA: ")
                modelo_modificado = f"{codigo},{nombre},{asignatura}\n"
                archivo_abierto.write(modelo_modificado)
                archivo_abierto.truncate()
                print(f"\n  DOCENTE {codigo} HA SIDO MODIFICADO \n")
            else:
                archivo_abierto.write(linea)
                archivo_abierto.truncate()
    except Exception as error:
        print(f"ERROR AL APLICAR LA MODIFICACION: {error}")


def modify_student():
    read_student()
    codigo = input("\n  INGRESE EL CODIGO DEL ESTUDIANTE A MODIFICAR: ")
    try:
        path="./alumnos.txt"
        archivo_abierto = open(path, mode="r+")
        lineas = archivo_abierto.readlines()
        archivo_abierto.seek(0)
        for linea in lineas:
            if codigo in linea:
                nombre = input("  Nombre: ")
                apellido = input("  Apellido: ")
                curso = input("  Curso: ")
                modelo_modificado = f"{codigo},{nombre},{apellido},{curso}\n"
                archivo_abierto.write(modelo_modificado)
                archivo_abierto.truncate()
                print(f"\n  ESTUDIANTE {codigo} HA SIDO MODIFICADO \n")
            else:
                archivo_abierto.write(linea)
                archivo_abierto.truncate()
    except Exception as error:
        print(f"ERROR AL APLICAR LA MODIFICACION: {error}")


def delete_docente():
    read_docente()
    codigo = input("\n  INGRESE EL CODIGO DEL DOCENTE A ELIMINAR: ")
    try:
        path="./docentes.txt"
        archivo_abierto = open(path, mode="r+")
        lineas = archivo_abierto.readlines()
        archivo_abierto.seek(0)
        for linea in lineas:
            if codigo in linea:
                modelo_vacio = "\n"
                archivo_abierto.write(modelo_vacio)
                archivo_abierto.truncate()
        print(f"\n HA SIDO ELIMINADO: {codigo} \n")
    except Exception as error:
        print(f"ERROR AL INTENTAR BORRAR AL DOCENTE: {error}")
        
        
def delete_student():
    read_student()
    codigo = input("\n  INGRESE EL CODIGO DEL ESTUDIANTE A ELIMINAR: ")
    try:
        path="./alumnos.txt"
        archivo_abierto = open(path, mode="r+")
        lineas = archivo_abierto.readlines()
        archivo_abierto.seek(0)
        for linea in lineas:
            if codigo in linea:
                modelo_vacio = "\n"
                archivo_abierto.write(modelo_vacio)
                archivo_abierto.truncate()
        print(f"\n HA SIDO ELIMINADO: {codigo} \n")
    except Exception as error:
        print(f"ERROR AL INTENTAR BORRAR AL ESTUDIANTE: {error}")


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

while True:
    Star_Aplication()
      
    opcionMenu = input("SELECCIONE UNA OPCION-> ")
            
    if opcionMenu=="1":
        print("1. \n  RESGISTRO DE DOCENTES")
        add_docente()
     
    elif opcionMenu=="2": 
        print("2. \n REGISTRO DE ESTUDIANTES")
        add_student()
        
    elif opcionMenu=="3":
        print("3. \n LISTA DE DOCENTES")
        read_docente()
          
    elif opcionMenu=="4":
        print("3. \n LISTA DE ESTUDIANTES")
        read_student()  
        
    elif opcionMenu=="5":
        print("3. \n MODIFICAR DOCENTES")
        modify_docente()
        
    elif opcionMenu=="6":
        print("3. \n MODIFICAR ESTUDIANTES")
        modify_student()
       
    elif opcionMenu=="7":
        print("3. \n ELIMINAR DOCENTE")
        delete_docente()
        
    elif opcionMenu=="8":
        print("3. \n ELIMINAR ESTUDIANTE")
        delete_student()
        
    elif opcionMenu=="9":
        break
        
    else:
        input("OPCION INCORRECTA...\nSELECCIONE NUEVAMENTE UNA OPCION")        



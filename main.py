from formulario import Formulario
from tipo_actividad import Actividad
from usuarios import Usuarios
from file_manager import FileManager


"""Agregar validación de horas por actividad / Y cuando el mes es 30 o 31 o 28"""
#Si es una validación solo es posible cargar 8 0 8 porque es en el mismo día
#Si es un retest son 3 dias por lo que uno puede cargar como máximo 24 0 24 y como minimo 8 16 24 o en el medio 16 8 24
#Si es un pentest el máximo es 40 0 40 el mínimo es 8 32 40 el segundo día es 16 24 40 el tercer día 24 16 40 el cuarto día 32 8 40

#Febrero es 28 días 02, 31 días 01/03/05/07/08/10/12 demas 30 dias LISTO

print("¡Bienvenido/a al sistema de carga de horas!")

fileManager = None

while True:

    respuesta = input("¿Quiere ingresar una nueva actividad? (Si/No): ")

    if respuesta == "Si":

        tipo_actividad = input("Ingrese el tipo de análisis (Pentest / Retest / Validación): ")
        tipo_actividad = Actividad(tipo_actividad)

        usuario = input("Ingrese el nombre y apellido del usuario que realiza la actividad: ")
        usuario = Usuarios(usuario)

        horas_realizadas = input("Ingrese las horas realizadas: ")
        horas_realizadas = int(horas_realizadas)

        horas_restantes = input("Ingrese las horas restantes: ")
        horas_restantes = int(horas_restantes)

        horas_totales = input("Ingrese las horas totales: ")
        horas_totales = int(horas_totales)

        fecha_inicio = input("Ingrese la fecha de inicio de la actividad (DD/MM/AA): ")
        fecha_fin = input("Ingrese la fecha de fin de la actividad (DD/MM/AA): ")
        

        formulario = Formulario(tipo_actividad,usuario, horas_realizadas,horas_restantes,horas_totales,fecha_inicio, fecha_fin)
        fileManager = FileManager(formulario)
        fileManager.validarFormulario()

    else:
        FileManager.csv_to_excel()
        print("Saliendo...")
        break




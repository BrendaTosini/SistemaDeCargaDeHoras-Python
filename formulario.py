from tipo_actividad import Actividad
from usuarios import Usuarios

class Formulario:

    def __init__(self, nombre_actividad:Actividad, nombre_usuario:Usuarios, horas_realizadas, horas_restantes, horas_totales, fecha_inicio, fecha_fin):
        
        self.nombre_actividad = nombre_actividad
        self.nombre_usuario = nombre_usuario
        self.horas_realizadas = horas_realizadas
        self.horas_restantes = horas_restantes
        self.horas_totales = horas_totales
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        

    
    def validar(self):

        if not isinstance(self.nombre_actividad, Actividad):
            print("Tipo de actividad inválido")

        if not isinstance(self.nombre_usuario, Usuarios):
            print("Nombre de usuario inválido")

        lista_errores = list()

        if self.nombre_actividad == "":
            lista_errores.append("El nombre_actividad no puede estar vacío")
        if self.nombre_usuario == "":
            lista_errores.append("El nombre_usuario no puede estar vacío")
        if self.horas_realizadas <= 0 or self.horas_realizadas > 40:
            lista_errores.append("Las horas_realizadas no pueden ser menor o igual a 0 o mayores a 40")
        if self.horas_restantes < 0 or self.horas_restantes > 40:
            lista_errores.append("Las horas_restantes no pueden ser menores a 0 o mayores a 40")
        if self.horas_totales < 8 or self.horas_totales > 40:
            lista_errores.append("Las horas_totales no pueden ser menor a 8 o mayor a 40")
        self.validar_fecha(self.fecha_inicio, lista_errores)
        self.validar_fecha(self.fecha_fin, lista_errores)

        if lista_errores:
            print("Formulario Inválido")
            print(lista_errores)
            return "Formulario Inválido"
        else:
            print("Formulario Creado con Exito")

    def validar_fecha(self, fecha:str , lista_errores:list):
        separar = fecha.split("/")
        if len(separar)!= 3:
            lista_errores.append("Fecha Inválida. El formato debe ser DD/MM/AA")
            return 
        dia = int(separar[0])
        mes = int(separar[1])
        año = int(separar[2])
        if dia < 1 or dia > 31:
            lista_errores.append("Día inválido. El día no puede ser menor a 1 o mayor a 31")

        if dia > 28 and mes == 2:
            lista_errores.append("Día inválido. Si es Febrero el día no puede ser mayor a 28")

        if mes < 1 or mes > 12:
            lista_errores.append("Mes inválido. El mes no puede ser menor a 1 o mayor a 12")

        meses_31 = [1,3,5,7,8,10,12]
        meses_30 = [2,4,6,9,11]    
        if dia == 31 and mes not in meses_31:
            lista_errores.append(f"Mes inválido. Los meses válidos con 31 dias son {meses_31}")
        if dia == 30 and mes not in meses_30:
            lista_errores.append(f"Mes inválido. Los meses válidos con 30 dias son {meses_30} ")

        if año != 26:
            lista_errores.append("Año inválido. Solo es válido el año vigente.")

    def get_categorias(self):
        lista_categorías = list()
        lista_categorías.append("Actividad")
        lista_categorías.append("Usuario")
        lista_categorías.append("Horas Realizadas")
        lista_categorías.append("Horas Restantes")
        lista_categorías.append("Horas Totales")
        lista_categorías.append("Fecha Inicio")
        lista_categorías.append("Fecha Fin")
        return lista_categorías
    
    def get_actividad(self):
        return str(self.nombre_actividad).replace("Actividad.", "")
    
    def get_usuario(self):
        return str(self.nombre_usuario).replace("Usuarios.", "")
    
    def get_horas_realizadas(self):
        return self.horas_realizadas
    
    def get_horas_restantes(self):
        return self.horas_restantes
    
    def get_horas_totales(self):
        return self.horas_totales
    
    def get_fecha_inicio(self):
        return self.fecha_inicio
    
    def get_fecha_fin(self):
        return self.fecha_fin

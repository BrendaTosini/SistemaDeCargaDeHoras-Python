import csv
import os
from formulario import Formulario
import pandas as pd

class FileManager:

    def __init__(self, formulario:Formulario):
        self.formulario = formulario
        
        if not isinstance(self.formulario, Formulario):
            print("Formulario Inválido")
            return None
        
    
    def validarFormulario(self):

        valido = self.formulario.validar()

        if valido != "Formulario Inválido":
            if not os.path.exists("formulario.csv"):
                self.crear_CSV()
            self.guardar_formulario()
        
        

    def crear_CSV(self):
        with open("formulario.csv", "w", newline="", encoding="utf-8") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=self.formulario.get_categorias(), delimiter=";")
            writer.writeheader()
    
    def guardar_formulario(self):
        with open("formulario.csv", "a", newline="", encoding="utf-8") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=self.formulario.get_categorias(), delimiter=";")
            writer.writerow({"Actividad": self.formulario.get_actividad(), "Usuario":self.formulario.get_usuario(), "Horas Realizadas": self.formulario.get_horas_realizadas(), "Horas Restantes": self.formulario.get_horas_restantes(), "Horas Totales": self.formulario.get_horas_totales(), "Fecha Inicio": self.formulario.get_fecha_inicio(), "Fecha Fin": self.formulario.get_fecha_fin()})

    @staticmethod
    def csv_to_excel():

        df = pd.read_csv("formulario.csv", sep=";")

        df_ordenado = df.sort_values(by="Usuario")

        df_ordenado.to_excel("tabla.xlsx", index=False)
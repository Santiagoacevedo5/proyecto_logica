#Mateo Ursuga 2/07/2025
from pelicula import Pelicula
import numpy as np
import datetime
from datetime import timedelta, date, time


class Funcion():

    pelicula=Pelicula
    fecha=datetime.date
    hora_inicio=datetime.time
    hora_fin=datetime.time
    matriz_asientos=np.ndarray

    def __init__(self):
        self.pelicula=None
        self.horario=""
        self.matriz_asientos=None

    def pedir_datos(self):
        while True:
            try:
                self.pelicula=input("Introduce el id de la película que quieres agregar a la función: ")
                self.fecha=datetime.datetime.strptime((input("Introduce la fecha de la función en formato DD-MM-YYYY: ")), "%d-%m-%Y")
                self.hora_inicio=datetime.datetime.strptime((input("Introduce la hora de inicio de la película en formato HH:MM: ")), "%H:%M")
                break
            except:
                print("Ingresa un dato válido.")
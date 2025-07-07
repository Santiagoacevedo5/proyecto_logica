from pelicula import Pelicula
import numpy as np
import datetime
from datetime import timedelta


class Funcion():

    pelicula=Pelicula
    fecha=datetime
    hora_inicio=datetime
    hora_fin=datetime
    matriz_asientos=np.ndarray

    def __init__(self):
        self.pelicula=None
        self.horario=""
        self.matriz_asientos=None

    def pedir_datos(self):
        self.pelicula=input("Introduce el id de la película que quieres agregar a la función: ")
        self.fecha=datetime.datetime.strptime((input("Introduce la fecha de la función en formato DD-MM-YYYY: ")), "%d-%m-%Y")
        self.hora_inicio=datetime.datetime.strptime((input("Introduce la hora de inicio de la película en formato HH:MM: ")), "%H:%M")
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
#        self.pelicula=input("Introduce el id de la pelicula que quieres agregar: ")
        self.fecha=datetime.datetime.strptime((input("Introduce la fecha de la funcion: ")), "%d-%m-%Y")
        self.hora_inicio=datetime.datetime.strptime((input("Introduce la hora de inicio de la pelicula: ")), "%H:%M")
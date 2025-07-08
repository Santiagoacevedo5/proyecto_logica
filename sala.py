# Hecha por Santiago Acevedo 01/7/2025 3:00pm
import numpy as np
from funcion import Funcion
class Sala():

    """Esta clase representa la plantilla para la creación de cada sala

    ATRIBUTOS:
    id: identificador de la sala
    valor_boleta: el valor de la boleta para la sala
    filas: el número de filas de la sala
    sillas_fila: el número de sillas por fila
    boletas_vendidas: el número de boletas vendidas en la sala
    MAX_PELICULAS: el número máximo de películas que puede tener la sala
    n_funciones: el número de funciones que tiene la sala
    programacion: un arreglo de funciones que representa la programación de la sala
    """
    id=int
    programacion=np.ndarray
    n_funciones=int
    valor_boleta=float
    filas=int
    sillas_fila=int
    boletas_vendidas=0

    MAX_PELICULAS=5

    def __init__(self):
        self.id=0
        self.n_funciones=0
        self.valor_boleta=0
        self.filas=0
        self.sillas_fila=0
        self.boletas_vendidas=0
        self.programacion=np.full((self.MAX_PELICULAS), fill_value=None, dtype=object)

    def pedir_datos(self):
        """Este método se encarga de pedir los datos y asignarlos a su atributo correspondiente"""
        while True:
            try:
                self.id=int(input("Introduce el id de la sala: "))
                self.filas=int(input("Introduce el numero de filas de la sala: "))
                self.sillas_fila=int(input("Introduce el numero de sillas en cada fila: "))
                self.valor_boleta=float(input("Introduce valor de la boleta para la sala: "))
                break
            except:
                print("Introduce un valor numérico.")

    def set_funcion_programacion(self, funcion):
        """Este método se encarga de asignar una funcion a la programación de la sala."""
        if self.n_funciones<5:
            self.programacion[self.n_funciones]=funcion
            self.n_funciones+=1
        else:
            print("Capacidad de la sala llena")

    def buscar_funcion(self, id):
        """Este método se encarga de buscar la posición de una función dentro de la lista de programación y retornar la posición"""
        for i in range(self.n_funciones):
            if self.programacion[i].pelicula.id==id:
                return i
        return -1
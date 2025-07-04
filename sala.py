#ESTA CLASE SIGUE EN DESARROLLO. AUN NO SE HA TERMINADO NI IMPLEMENTADO
import numpy as np
from funcion import Funcion
class Sala():

    """Esta clase representa la plantilla para la creación de cada sala

    ATRIBUTOS:
    id: identificador de la sala
    tamaño: el tamaño de la sala enterminos de sillas
    programación: la programación de películas de la sala
    n_peliculas: número de películas que tiene la sala
    """
    id=int
    programacion=np.ndarray
    n_funciones=int
    valor_boleta=float
    filas=int
    sillas_fila=int

    MAX_PELICULAS=5

    def __init__(self):
        self.id=0
        self.n_funciones=0
        self.valor_boleta=0
        self.filas=0
        self.sillas_fila=0
        self.programacion=np.full((self.MAX_PELICULAS), fill_value=None, dtype=object)

    def pedir_datos(self):
        """Este método se encarga de pedir los datos y asignarlos a su atributo correspondiente"""
        self.id=int(input("Introduce el id de la sala: "))
        self.filas=int(input("Introduce el numero de filas de la sala: "))
        self.sillas_fila=int(input("Introduce el numero de sillas en cada fila: "))
        self.valor_boleta=float(input("Introduce valor de la boleta para la sala: "))
#        n=int(input("Ingresa cuantas películas deseas añadir a la programacion de esta sala. (0-5): "))
#        while n<0 or n>5:
#            print("El número de películas que elgiste no esta dentro del rango. Intentalo de nuevo")
#            n=int(input("Ingresa cuantas películas deseas añadir a la programacion de esta sala. (0-5): "))
#        for _ in range(n):
#            self.programacion.pedir_datos()

    def set_funcion_programacion(self, funcion):
        if self.n_funciones<5:
            self.programacion[self.n_funciones]=funcion
            self.n_funciones+=1
        else:
            print("Capacidad de la sala llena")

    def buscar_funcion(self, id):
        for i in range(self.n_funciones):
            if self.programacion[i].pelicula.id==id:
                return i
        return -1
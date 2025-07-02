#ESTA CLASE SIGUE EN DESARROLLO. AUN NO SE HA TERMINADO NI IMPLEMENTADO
import numpy as np
import programacion as Programacion
class Sala():

    """Esta clase representa la plantilla para la creación de cada sala

    ATRIBUTOS:
    id: identificador de la sala
    tamaño: el tamaño de la sala enterminos de sillas
    programación: la programación de películas de la sala
    """
    id=int
    tamano=int
    programacion=Programacion

    TAMAÑO=36

    def __init__(self):
        self.id=0
        self.tamano=self.TAMAÑO

    def pedir_datos(self):
        """Este método se encarga de pedir los datos y asignarlos a su atributo correspondiente"""
        self.id=int(input("Introduce el id de la sala: "))

        n=int(input("Ingresa cuantas películas deseas añadir a la programacion de esta sala. (0-5): "))
        while n<0 or n>5:
            print("El número de películas que elgiste no esta dentro del rango. Intentalo de nuevo")
            n=int(input("Ingresa cuantas películas deseas añadir a la programacion de esta sala. (0-5): "))
        self.programacion.pedir_datos(n)
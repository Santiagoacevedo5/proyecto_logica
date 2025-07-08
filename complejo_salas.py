<<<<<<< HEAD
#Jesica Estor 20/06/2025
=======
# Mateo Ursuga 30/6/2025 10:00am
>>>>>>> bbd03f7f3c829d8fcdba860f221d72ae82b5c7f1
import numpy as np
class Complejo_Salas():

    """Esta clase representa la plantilla para la creación del complejo de salas

    ATRIBUTOS:
    nombre: Nombre del complejo
    direccion: Dirección del complejo
    lista_salas: Lista con las salas de cine que contiene el complejo
    """
    nombre=str
    direccion=str
    lista_salas=np.ndarray

    MAX_SALAS=12

    def __init__(self):
        self.nombre=""
        self.direccion=""
        self.lista_salas=np.full((self.MAX_SALAS), fill_values=None, dtype=object)
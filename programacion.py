#Jesica Estor 2/07/2025
from datetime import datetime, timedelta
import numpy as np
import pelicula as Pelicula
import sala as Sala 
import math

class Programacion:
    """
    Clase que maneja la programación semanal de películas en múltiples salas.
    Cada función contiene: una película, un objeto Sala, hora de inicio, fin y mapa de asientos.
    ATRIBUTOS 
     peliculas =a rreglo de objetos Pelicula
     salas = arreglo de objetos Sala
     inicios = arreglo de objetos datetime (inicio de la función)
     fines = arreglo de objetos datetime (fin de la función)
     contador = cantidad de funciones almacenadas
    CONSTANTE
     MAX_DE_PROGRAMACIONES = Tamaño de los arreglos, reprsenta el # máximo de funciones que pueden ser almacenadas
    """

    MAX_DE_PROGRAMACIONES = 1000
    peliculas = np.ndarray
    salas = np.ndarray  
    inicios = np.ndarray
    fines = np.ndarray
    contador = int

    def __init__(self):
        self.peliculas = np.full(self.MAX_DE_PROGRAMACIONES, None, dtype=object)
        self.salas = np.full(self.MAX_DE_PROGRAMACIONES, None, dtype=object) 
        self.inicios = np.full(self.MAX_DE_PROGRAMACIONES, None, dtype=object)
        self.fines = np.full(self.MAX_DE_PROGRAMACIONES, None, dtype=object)
        self.asientos = np.full(self.MAX_DE_PROGRAMACIONES, None, dtype=object)
        self.contador = 0

    def guardar_funcion(self, pelicula, sala, inicio):
        """
        Guarda una función si no hay traslapes en la misma sala y crea un mapa por función.
        RETORNA
        True si se pudo guardar, False en caso contrario
        """

        fin = inicio + timedelta(minutes=pelicula.duracion)

        for i in range(self.contador):
            sala_existente = self.salas[i]
            if sala_existente != None and sala_existente.id == sala.id:
                if not (fin <= self.inicios[i] or inicio >= self.fines[i]):
                    print(f"Error Traslape con '{self.peliculas[i].nombre_es}' en sala {sala.id}.")
                    return False

        if self.contador < self.MAX_DE_PROGRAMACIONES:
            self.peliculas[self.contador] = pelicula
            self.salas[self.contador] = sala
            self.inicios[self.contador] = inicio
            self.fines[self.contador] = fin
            filas = int(math.sqrt(sala.tamano))
            columnas = math.ceil(sala.tamano / filas)
            mapa = np.zeros((filas, columnas), dtype=int)
            self.asientos[self.contador] = mapa
            self.contador += 1
            print(f"{pelicula.nombre_es}' programada en sala {sala.id}.")
            return True
        
        else:
            print("Error! limite de funciones alcanzado")
            return False

    def mostrar_programacion(self):
        """
        Muestra todas las funciones programadas.
        """
        if self.contador == 0:
            print("No hay funciones programadas.")
            return

        for i in range(self.contador):
            print(f"Sala {self.salas[i].id} -- {self.peliculas[i].nombre_es}: {self.inicios[i]} - {self.fines[i]}")

    def eliminar_funcion(self, pelicula_id):
        """
        Elimina todas las funciones de una película por su ID.
        """
        nuevas_peliculas = np.full(self.MAX_DE_PROGRAMACIONES, None, dtype=object)
        nuevas_salas = np.full(self.MAX_DE_PROGRAMACIONES, None, dtype=object)
        nuevas_inicios = np.full(self.MAX_DE_PROGRAMACIONES, None, dtype=object)
        nuevas_fines = np.full(self.MAX_DE_PROGRAMACIONES, None, dtype=object)

        nuevo_contador = 0

        for i in range(self.contador):
            if self.peliculas[i].id != pelicula_id:
                nuevas_peliculas[nuevo_contador] = self.peliculas[i]
                nuevas_salas[nuevo_contador] = self.salas[i]
                nuevas_inicios[nuevo_contador] = self.inicios[i]
                nuevas_fines[nuevo_contador] = self.fines[i]
                nuevo_contador += 1

        self.peliculas = nuevas_peliculas
        self.salas = nuevas_salas
        self.inicios = nuevas_inicios
        self.fines = nuevas_fines
        self.contador = nuevo_contador

        print(f"Se eliminaron funciones de la película con ID {pelicula_id}.")

    def ocupar_asiento(self, indice_funcion, fila, columna):
        """
        Ocupa un asiento específico en una función programada.
        """
        if 0 <= indice_funcion < self.contador:
            mapa = self.asientos[indice_funcion]

            if 0 <= fila < len(mapa) and 0 <= columna < len(mapa[0]):
                if mapa[fila, columna] == 0:
                    mapa[fila, columna] = 1
                    print(f"Asiento ({fila}, {columna}) ocupado correctamente.")
                else:
                    print("Ese asiento ya está ocupado.")
            else:
                print("Posición fuera del rango del mapa.")
        else:
            print("Índice de función inválido.")


    def renovar_programacion(self):
        """
        Borra toda la programación.
        """
        self.__init__()
        print("Programación semanal renovada.")

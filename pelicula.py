import numpy as np
class Pelicula():

    """Esta clase representa la plantilla para la creación de cada película.

    ATRIBUTOS:
    id: Identificador de la película
    nombre_es: Nombre de la película en español.
    duracion: Duración de la película en minutos.
    nombre_or: Nombre original de la película.
    año_estreno: Año en que se estrenó la película.
    genero: Género de la película.
    pais_estreno: El país donde se estreno la película.
    activa: Este atributo sirve para saber si la película esta activa o no.
    calificación: valoración de la película.
    """
    id=int
    nombre_es=str
    duracion=int
    nombre_or=str
    año_estreno=int
    genero=str
    pais_estreno=str
    activa=int
    calificacion=int

    def __init__(self):
        self.id=0
        self.nombre_es=""
        self.duracion=0
        self.nombre_or=""
        self.año_estreno=0
        self.genero=""
        self.pais_estreno=""
        self.activa=1
        self.calificacion=""

    def pedir_datos(self):
        """Este método pide los datos de la película y los asigna a su atributo correspondiente."""
        while True:
            try:
                self.id=int(input("Introduce el id de la película: "))
                self.nombre_es=input("Introduce el nombre en español de la película: ")
                self.duracion=int(input("Introduce la duración de la película en minutos: "))
                self.nombre_or=input("Introduce el nombre original de la película: ")
                self.año_estreno=int(input("Introduce el año de estreno de la película: "))
                self.genero=input("Introduce el género de la película: ")
                self.pais_estreno=input("Introduce el país de estreno de la película: ")
                self.activa=int(input("Introduce el estado de la película:\n1.Activa\n2.No Activa\nOpción: "))
                while self.activa!=1 and self.activa!=2:
                    print("Opción no valida. Intentalo de nuevo.")
                    self.activa=int(input("Introduce si la película esta activa:\n1.SI\n2.NO\nOpción: "))
                self.calificacion=int(input("Introduce una valoración de la película entre 1-10: "))
                break
            except:
                print("Ingresa un dato válido.")
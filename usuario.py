import numpy as np
class Usuario():

    """Esta clase representa la plantilla para crear cada usuario

    ATRIBUTOS:
    nombre: Nombre del usuario
    id: Identificador del usuario
    email: Email de contacto del usuario
    tipo: Tipo de usuario (CLIENTE, ADMIN, VENDEDOR)
    contraseña: Contraseña del usuario

    CONSTANTES:
    PERFIL_CLIENTE: Representa el tipo de perfil del cliente
    PERFIL_ADMIN: Representa el tipo de perfil del admin
    PERFIL_VENDEDOR: Representa el tipo de perfil del vendedor
    """
    nombre=str
    id=int
    email=str
    tipo=int
    contraseña=str

    PERFIL_CLIENTE=1
    PERFIL_ADMIN=2
    PERFIL_VENDEDOR=3

    def __init__(self, nombre="", id=0, email="", contrasena=""):
        self.nombre=nombre
        self.id=id
        self.email=email
        self.contrasena=contrasena
        self.tipo=self.PERFIL_CLIENTE

    def pedir_datos(self):
        """Este método se encarga de pedir los datos por consola y asignarlos a cada uno de los atributos correspondientes"""
        while True:
            try:
                self.id=int(input("Introduce tu id: "))
                self.nombre=input("Introduce tu nombre: ")
                self.email=input("Introduce tu email: ")
                self.contrasena=input("Introduce la contraseña del usuario: ")
                break
            except:
                print("Ingresa un dato válido.")

    def cambiar_tipo(self, tipo):
        """Este método se encarga de asignar el tipo de usuario. Por defecto es de tipo PERFIL_CLIENTE"""
        self.tipo=tipo
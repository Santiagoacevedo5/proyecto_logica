import usuario as Usuario
import programacion as Programacion
import pelicula as Pelicula
import numpy as np
class AppCine():
    "a"
    """Esta clase representa la plantilla principal del programa en donde se ejecuta la aplicación

    ATRIBUTOS:
    usuarios: Los usuarios de la aplicación
    n_usuarios: Número de usuarios en la aplicación
    usuario_autenticado: Usuario que esta autenticado
    peliculas: Películas que hay en la aplicación
    n_peliculas: Número de películas que hay dentro de la aplicacíon
    programaciones: Programaciones para las salas y complejos de cine
    n_programaciones: Número de programaciones
#SAPOS PERROS

    CONTANTES:
    MAX_USUARIOS: Máximo de usuarios que pueden existir en la aplicación
    MAX_PELICULAS: Máximo de películas que pueden existir en la aplicación
    """
    usuarios=np.ndarray
    n_usuarios=int
    usuario_autenticado=Usuario
    peliculas=np.ndarray
    n_peliculas=int
    programaciones=np.ndarray
    n_programaciones=0

    MAX_USUARIOS=30
    MAX_PELICULAS=40

    def __init__(self):
        self.usuarios=np.full((self.MAX_USUARIOS), fill_value=None, dtype=object)
        self.peliculas=np.full((self.MAX_PELICULAS), fill_value=None, dtype=object)

        self.usuarios[0]=Usuario("Sofia", 123, "sofia@udea.edu.co", "hola123")
        self.usuarios[0].cambiar_tipo(Usuario.PERFIL_ADMIN)

        self.usuarios[1]=Usuario("Juan", 456, "juan@udea.edu.co", "juan123")
        self.usuarios[1].cambiar_tipo(Usuario.PERFIL_VENDEDOR)
        self.n_usuarios=2
        self.usuario_autenticado=None
        self.n_peliculas=0

    def registrar_usuario(self):
        """Este método se encarga de registrar nuevos usuarios"""
        usuario=Usuario()
        usuario.pedir_datos()
        self.usuarios[self.n_usuarios]=usuario
        self.n_usuarios+=1

    def autenticar_usuario(self):
        """Este método se encarga de autenticas y validar la informacion de los usuarios que estan entrando a la aplicación"""
        print("\n%% AUTENTICAR USUARIO %%\n")
        id=int(input("Introduce el id del usuario: "))
        contraseña=input("Introduce la contraseña del usuario: ")

        for j in range(self.n_usuarios):
            if self.usuarios[j].id==id:
                if self.usuarios[j].contraseña==contraseña:
                    self.usuario_autenticado=self.usuarios[j]
                    return True
                else:
                    print("La contraseña ingresada es incorrecta")
                    return False
        print("Usuario no registrado")
        return False

    def crear_pelicula(self):
        """Este método se encarga de crear películas dentro del sistema"""
        nueva_pelicula=Pelicula()
        nueva_pelicula.pedir_datos()
        self.peliculas[self.n_peliculas]=nueva_pelicula
        print("PELICULA CREADA CON EXITO!!!!")
        self.n_peliculas+=1

    def modificar_pelicula(self):
        """Este método se encarga de modificar el estado de una película a activa/inactiva según corresponda"""
        self.mostrar_total_peliculas()
        op=int(input("Introduce el id de la peíicula que quieres modificar: "))
        for i in range(self.n_peliculas):
            if self.peliculas[i].id==op:
                if self.peliculas[i].activa==1:
                    print("Estado actual de la película: Activa\nIntroduce el nuevo estado de la película \n1.Activa\n2. No activa")
                    self.peliculas[i].activa=int(input("Introduce la opcion: "))
                    return
                else:
                    print("Estado actual de la película: No Activa\nIntroduce el nuevo estado de la película \n1.Activa\n2. No activa")
                    self.peliculas[i].activa=int(input("Introduce la opción: "))
                    return
        print("Película no encontrada")
        return

    def mostrar_total_peliculas(self):
        for i in range(self.n_peliculas):
            print(f"{i+1}. Nombre: {self.peliculas[i].nombre_es}.   ID: {self.peliculas[i].id}")

    def eliminar_pelicula(self):
        """Este método se encarga de eliminar películas ya existentes en el sistema"""
        self.mostrar_peliculas_activas()
        id_eliminar=-1
        op=int(input("Introduce el id de la película que quieres modificar: "))
        for j in range(self.n_peliculas):
            if self.peliculas[j].id==op:
                id_eliminar=j
        if id_eliminar!=-1:
            self.peliculas[id_eliminar]=None

            for i in range(id_eliminar+1, self.n_peliculas):
                self.peliculas[i-1]=self.peliculas[i]
            #self.peliculas[i]=None
            self.n_peliculas-=1
            return True
        else:
            return False

    def mostrar_detalles_pelicula(self):
        """Este método se encarga de mostrar al usuario los detalles de la película que esta consultando"""
        if self.mostrar_peliculas_activas()!=False:
            op=int(input("Introduce el id de la película que quieres consultar: "))
            for i in range(self.n_peliculas):
                if self.peliculas[i].id==op:
                    if self.peliculas[i].activa==1:
                        print(f"\n1. ID: {self.peliculas[i].id}\nNombre en español: {self.peliculas[i].nombre_es}\n3. Duración: {self.peliculas[i].duracion}\n4. Nombre original: {self.peliculas[i].nombre_or}\n5. Año de estreno: {self.peliculas[i].año_estreno}\n6. País de estreno: {self.peliculas[i].pais_estreno}\n7. Género: {self.peliculas[i].genero}\n8.Estado: Activa\n9. Calificacion: {self.peliculas[i].calificacion}")
                    else:
                        print(f"\n1. ID: {self.peliculas[i].id}\nNombre en español: {self.peliculas[i].nombre_es}\n3. Duración: {self.peliculas[i].duracion}\n4. Nombre original: {self.peliculas[i].nombre_or}\n5. Año de estreno: {self.peliculas[i].año_estreno}\n6. País de estreno: {self.peliculas[i].pais_estreno}\n7. Género: {self.peliculas[i].genero}\n8.Estado: Activa\n9. Calificacion: {self.peliculas[i].calificacion}")

    def mostrar_peliculas_activas(self):
        """Este método muestra la lista de películas activas actualmente en el sistema"""
        print("\n%% Películas disponibles %%")
        peliculas_activas_count = 0
        for i in range(self.n_peliculas):
            pelicula = self.peliculas[i]
            if pelicula is not None and pelicula.activa == 1:
                peliculas_activas_count += 1
                print(f"{peliculas_activas_count}. Nombre: {pelicula.nombre_es}, ID: {pelicula.id}")
        """Si no existe ninguna película activa, mostrar el mensaje que indique la ausencia de las mismas"""
        if peliculas_activas_count == 0:
            print("No hay películas activas para mostrar.")
            return False

    """def crear_programacion(self):
        self.programaciones[self.n_programaciones]=Programacion()
        print("\n%% Peliculas disponibles para añadir a la programacion %%")
        numerador=0
        for i in range(self.n_peliculas):
            if self.peliculas[i].activa==1:
                numerador+=1
                print(f"{numerador}. Nombre: {self.peliculas[i].nombre_es}, ID: {self.peliculas[i].id}")
        self.programaciones[self.n_programaciones].pedir_datos()"""

    def mostrar_menu_admin(self):
        """Este método muestra las opciones dentro del menú del administrador"""
        opcion=0
        while opcion!=15:
            print("\n%% MENÚ DE OPCIONES USUARIO ADMIN %%\n")
            print("1. Crear Película\n2. Mostrar detalles de película\n3. Modificar película\n4. Eliminar Película\n5. Crear Programación\n6. Modificar Programación\n7. Eliminar Programación\n8. Crear Sala\n9. Modificar Sala\n10. Eliminar Sala\n11. Crear Cliente\n12. Eliminar Cliente\n13. Consultar ganancias de una sala\n14. Consultar ganancias de un complejo\n15. Consultar % de ocupación de una película\n16 Cerrar sesión")
            opcion=int(input("Introduce la opción que deseas: "))
            match(opcion):
                case 1:
                    self.crear_pelicula()
                case 2:
                    self.mostrar_detalles_pelicula()
                case 3:
                    self.modificar_pelicula()
                case 4:
                    self.eliminar_pelicula()

                case 16:
                    break


    def procesar(self):
        op=0

        while op!=3:
            print ("\n%% MENÚ DE APLICACIÓN %%\n")
            print("1. Registrarse \n2. Auntenticarse \n3. Salir de la app")
            op=int(input("Seleccione una opción del menú: "))
            match(op):
                case 1:
                    self.registrar_usuario()
                case 2:
                    if self.autenticar_usuario():
                        if self.usuario_autenticado.tipo==Usuario.PERFIL_ADMIN:
                            self.mostrar_menu_admin()

                case 3:
                    self.usuario_autenticado=None
                    print("Aplicación terminada")


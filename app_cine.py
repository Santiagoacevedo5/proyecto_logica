from usuario import Usuario
from funcion import Funcion
from pelicula import Pelicula
import numpy as np
from sala import Sala
from programacion import Programacion
from datetime import date, timedelta
import pickle

class AppCine():
    """Esta clase representa la plantilla principal del programa en donde se ejecuta la aplicación

    ATRIBUTOS:
    usuarios: Los usuarios de la aplicación
    n_usuarios: Número de usuarios en la aplicación
    usuario_autenticado: Usuario que esta autenticado
    peliculas: Películas que hay en la aplicación
    n_peliculas: Número de películas que hay dentro de la aplicacíon
    programaciones: Programaciones para las salas y complejos de cine
    n_programaciones: Número de programaciones


    CONTANTES:
    MAX_USUARIOS: Máximo de usuarios que pueden existir en la aplicación
    MAX_PELICULAS: Máximo de películas que pueden existir en la aplicación
    """
    usuarios=np.ndarray
    n_usuarios=int
    usuario_autenticado=Usuario
    peliculas=np.ndarray
    n_peliculas=int
    programacion=Programacion
    salas=np.ndarray
    n_salas=int

    MAX_USUARIOS=30
    MAX_PELICULAS=40
    MAX_SALAS=10
#Mateo Ursuga 2/07/2025
    def __init__(self):
        self.usuarios=np.full((self.MAX_USUARIOS), fill_value=None, dtype=object)
        self.peliculas=np.full((self.MAX_PELICULAS), fill_value=None, dtype=object)
        self.salas=np.full((self.MAX_SALAS), fill_value=None, dtype=object)

        self.usuarios[0]=Usuario("Sofia", 123, "sofia@udea.edu.co", "hola123")
        self.usuarios[0].cambiar_tipo(Usuario.PERFIL_ADMIN)

        self.usuarios[1]=Usuario("Juan", 456, "juan@udea.edu.co", "juan123")
        self.usuarios[1].cambiar_tipo(Usuario.PERFIL_VENDEDOR)
        self.n_usuarios=2
        self.usuario_autenticado=None
        self.n_peliculas=0
        self.n_salas=0
        self.programacion=Programacion()
#Mateo Ursuga 2/07/2025
    def registrar_usuario(self):
        """Este método se encarga de registrar nuevos usuarios"""
        usuario=Usuario()
        usuario.pedir_datos()
        for i in range(self.n_usuarios):
            if self.usuarios[i].id==usuario.id or self.usuarios[i].email==usuario.email or self.usuarios[i].contrasena==usuario.contrasena:
                print("Usuario ya existente. Introduce un usuario nuevo.")
                usuario.pedir_datos
        self.usuarios[self.n_usuarios]=usuario
        self.n_usuarios+=1
        self.guardar_datos()
#Mateo Ursuga 3/07/2025
    def autenticar_usuario(self):
        """Este método se encarga de autenticas y validar la informacion de los usuarios que estan entrando a la aplicación"""
        print("\n%% AUTENTICAR USUARIO %%\n")
        try:
            id=int(input("Introduce el id del usuario: "))
            contraseña=input("Introduce la contraseña del usuario: ")

            for j in range(self.n_usuarios):
                if self.usuarios[j].id==id:
                    if self.usuarios[j].contrasena==contraseña:
                        self.usuario_autenticado=self.usuarios[j]
                        return True
                    else:
                        print("La contraseña ingresada es incorrecta")
                        return False
            print("Usuario no registrado")
            return False
        except:
            print("Ingresa un dato válido.")
    #Mateo Ursuga 4/07/2025
    def mostrar_clientes(self):
        for i in range(self.n_usuarios):
            if self.usuarios[i].tipo==1:
                print("ID: ", self.usuarios[i].id, " - Nombre: ", self.usuarios[i].nombre)
#Mateo Ursuga 28/06/2025
    def eliminar_usuario(self):
        """Este método se encarga de eliminar usuarios."""
        self.mostrar_clientes()
        try:
            id_cliente=int(input("Introduce el id del cliente que deseas eliminar: "))
            us=self.buscar_usuario(id_cliente)
            if us!=-1:
                for _ in range(self.n_usuarios-1):
                    self.usuarios[us]=self.usuarios[us+1]
                self.usuarios[self.n_usuarios-1]=None
                self.n_usuarios-=1
                print("Usuario eliminado con éxito.")
                return True
            return False
        except ValueError:
            print("Introduce un valor numérico.")
#Mateo Ursuga 2/07/2025
    def buscar_usuario(self, id):
        for i in range(self.n_usuarios):
            if self.usuarios[i].id==id:
                return i
        return -1 
    
        
#Mateo Ursuga 2/07/2025
    def crear_pelicula(self):
        """Este método se encarga de crear películas dentro del sistema"""
        nueva_pelicula=Pelicula()
        nueva_pelicula.pedir_datos()
        self.peliculas[self.n_peliculas]=nueva_pelicula
        print("PELICULA CREADA CON EXITO!!!!")
        self.n_peliculas+=1
        self.guardar_datos()
#Mateo Ursuga 2/07/2025
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
        self.guardar_datos()
        return
#Mateo Ursuga 2/07/2025
    def mostrar_total_peliculas(self):
        for i in range(self.n_peliculas):
            print(f"{i+1}. Nombre: {self.peliculas[i].nombre_es}.   ID: {self.peliculas[i].id}")
#Mateo Ursuga 2/07/2025
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
            self.guardar_datos()
            return True
        else:
            return False
#Mateo Ursuga 2/07/2025
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
#Mateo Ursuga 2/07/2025
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
#Jesica Estor 2/07/2025
    def mostrar_menu_admin(self):
        """Este método muestra las opciones dentro del menú del administrador"""
        opcion=0
        while opcion!=15:
            print("\n%% MENÚ DE OPCIONES USUARIO ADMIN %%\n")
            print("1. Crear Película\n2. Mostrar detalles de película\n3. Modificar película\n4. Eliminar Película\n5. Crear Función\n6. Modificar Función\n7. Eliminar Función\n8. Crear Sala\n9. Modificar Sala\n10. Eliminar Sala\n11. Crear Cliente\n12. Eliminar Cliente\n13. Consultar % de ocupación de una película\n14. Consultar programación del complejo completo \n15. Consultar programación de una película \n16. Modificar programación de una sala\n17. Consultar ganancias de una sala o complejo\n18. Salir")
            opcion=int(input("Introduce la opción que deseas: "))
            try:
                match(opcion):
                    case 1:
                        self.crear_pelicula()
                    case 2:
                        self.mostrar_detalles_pelicula()
                    case 3:
                        self.modificar_pelicula()
                    case 4:
                        self.eliminar_pelicula()
                    case 5:
                        self.annadir_pelicula_funcion()
                    case 6:
                        self.modificar_funcion()
                    case 7:
                        self.eliminar_funcion_sala()
                    case 8:
                        self.crear_sala()
                    case 9:
                        self.modificar_sala()
                    case 10:
                        self.eliminar_sala()
                    case 11:
                        self.registrar_usuario()
                    case 12:
                        self.eliminar_usuario()
                    case 13:
                        self.consultar_ocupacion_pelicula()
                    case 14:
                        self.consultar_programacion_complejo()
                    case 15:
                        self.consultar_programacion_pelicula()
                    case 16:
                        self.modificar_programacion_sala()
                    case 17:
                        self.consultar_ganancias_sala_o_complejo()
                    case 18:
                        break
                    case _:
                        if opcion<1 or opcion>19:
                            print("Opción no válida. Por favor, introduce un número entre 1 y 19.")
            except ValueError:
                    print("Entrada inválida. Por favor, introduce un número entero: ")
#Jesica Estor 2/07/2025
    def consultar_programacion_complejo(self):
        """Este método se encarga de consultar la programación de un complejo"""
        for i in range(self.n_salas):
            print(f"Sala {self.salas[i].id}:")
            for j in range(self.salas[i].n_funciones):
                funcion = self.salas[i].programacion[j]
                print(f"  - {funcion.pelicula.nombre_es} ({funcion.fecha.date()}) - {funcion.hora_inicio.strftime('%H:%M')} a {funcion.hora_fin.strftime('%H:%M')}")    
#Jesica Estor 2/07/2025  
    def consultar_programacion_pelicula(self):
        """Este método se encarga de consultar la programación de una película en todas las salas"""
        # santiago acevedo 05/7/2025 
        self.mostrar_peliculas_activas()
        while True:
            try:
                id_pelicula = int(input("Introduce el id de la película que deseas consultar (o -1 para salir): "))
                if id_pelicula == -1:
                    break
                encontrado = False
                for i in range(self.n_salas):
                    for j in range(self.salas[i].n_funciones):
                        if self.salas[i].programacion[j].pelicula.id == id_pelicula:
                            funcion = self.salas[i].programacion[j]
                            print(f"Sala {self.salas[i].id}: {funcion.pelicula.nombre_es} - {funcion.fecha.date()} - {funcion.hora_inicio.strftime('%H:%M')} a {funcion.hora_fin.strftime('%H:%M')}")
                            encontrado = True

                if not encontrado:
                    print("No se encontraron funciones para la película con el ID proporcionado.")
                    input("Presiona Enter para intentar de nuevo...")

                else:
                    input("Presiona Enter para volver al menú...")
                    break  # Se encontró la película, salimos del bucle

            except ValueError:
                print("ID de película inválido. Por favor, introduce un número entero.")
            
    def consultar_ocupacion_pelicula(self):
        """Este método se encarga de consultar el porcentaje de ocupación de una película en todas las salas"""
        #santiago acevedo 05/7/2025 
        self.mostrar_peliculas_activas()
        try:
            id_pelicula=int(input("Introduce el id de la película que deseas consultar: "))
            for i in range(self.n_salas):
                for j in range(self.salas[i].n_funciones):
                    if self.salas[i].programacion[j].pelicula.id==id_pelicula:
                        funcion = self.salas[i].programacion[j]
                        ocupacion = (self.salas[i].boletas_vendidas / (self.salas[i].filas*self.salas[i].sillas_fila)) * 100
                        print(f"Sala {self.salas[i].id}: {funcion.pelicula.nombre_es} - {ocupacion}% de ocupación")
        except ValueError:
            print("ID de película inválido. Por favor, introduce un número entero: ")
#Jesica Estor 3/07/2025
    def modificar_programacion_sala(self):
        """Este método se encarga de modificar la programación de una sala"""
        self.mostrar_salas_disponibles()
        try:
            id_sala=int(input("Introduce el id de la sala que deseas modificar: "))
            busqueda_sala=self.buscar_sala(id_sala)
            if busqueda_sala!=-1:
                self.salas[busqueda_sala].buscar_funcion(id_sala)
                try:
                    id_funcion=int(input("Introduce el id de la función que deseas modificar: "))
                    funcion=self.salas[busqueda_sala].buscar_funcion(id_funcion)
                    if funcion!=-1:
                        nueva_funcion=Funcion()
                        nueva_funcion.pedir_datos()
                        self.salas[busqueda_sala].programacion[funcion]=nueva_funcion
                        print("Función modificada correctamente.")
                    else:
                        print("Función no encontrada.")
                except ValueError:
                    print("ID de función inválido. Por favor, introduce un número entero: ")
            else:
                print("Sala no encontrada.")
        except ValueError:
            print("ID de sala inválido. Por favor, introduce un número entero: ")
#Mateo Ursuga 2/07/2025        
    def modificar_sala(self):
        """Este método se encarga de modificar una sala dada."""
        self.mostrar_salas_disponibles()
        try:
            id_sala=int(input("Introduce el id de la sala que deseas modificar: "))
            sa=self.buscar_sala(id_sala)
            if sa!=-1:
                print("Valor actual de la boleta: ", self.salas[sa].valor_boleta)
                try:
                    valor_nuevo=float(input("Ingresa el nuevo valor de la boleta: "))
                    self.salas[sa].valor_boleta=valor_nuevo
                except:
                    print("Ingresa un dato válido")
            else:
                print("Sala no encontrada")
        except:
            print("Ingresa un valor válido")
#Mateo Ursuga 2/07/2025        
    def eliminar_sala(self):
        """Este método se encarga de eliminar una sala dada."""
        self.mostrar_salas_disponibles()
        try:
            id_sala=int(input("Ingrese el id de la sala que deseas eliminar: "))
            sa=self.buscar_sala(id_sala)
            if sa!=-1:
                for _ in range(self.n_salas-1):
                    self.salas[sa]=self.salas[sa+1]
                self.salas[self.n_salas-1]=None
                self.n_salas-=1
                print("Se eliminó la sala correctamente.")
                return True
            else:
                print("Sala no encontrada.")
                return False
        except:
            print("Ingrese un dato válido.")
#Jesica Estor 5/07/2025
    def consultar_ganancias_sala_o_complejo(self):
        """Este método se encarga de consultar las ganancias de una sala o complejo"""
        print("1. Consultar ganancias de una sala\n2. Consultar ganancias de un complejo")
        try:
            opcion=int(input("Selecciona una opción: "))
            if opcion==1:
                self.mostrar_salas_disponibles()
                id_sala=int(input("Introduce el id de la sala que deseas consultar: "))
                busqueda_sala=self.buscar_sala(id_sala)
                if busqueda_sala!=-1:
                    total_ganancias = 0
                    for funcion in self.salas[busqueda_sala].programacion:
                        if funcion is not None:
                            total_ganancias += self.salas[busqueda_sala].boletas_vendidas*self.salas[busqueda_sala].valor_boleta
                    print(f"Ganancias de la sala {self.salas[busqueda_sala].id}: ${total_ganancias}")
                else:
                    print("Sala no encontrada.")
            elif opcion==2:
                total_ganancias = 0
                for sala in self.salas:
                    if sala is not None:
                        for funcion in sala.programacion:
                            if funcion is not None:
                                total_ganancias += sala.boletas_vendidas * sala.valor_boleta
                print(f"Ganancias del complejo: ${total_ganancias}")
            else:
                print("Opción no válida.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero: ")
#Jesica Estor 5/07/2025
    def mostrar_menu_cliente(self):
        """Este método se encarga de mostrar el menú del cliente"""
        opcion=0
        while opcion!=6:
            print("\n%% MENÚ DE OPCIONES CLIENTE %%\n")
            print("1. Ver función de una sala\n2. Ver función de un complejo\n3. Ver programación de una película\n4. Consultar detalles de una película\n5. Reservar boleta\n6. Salir")
            opcion=int(input("Introduce la opcion que deseas: "))
            match(opcion):
                case 1:
                    self.mostrar_funciones_sala()
                case 2:
                    self.consultar_programacion_complejo()
                case 3:
                    self.consultar_programacion_pelicula()
                case 4:
                    self.mostrar_detalles_pelicula()
                case 5:
                    self.reservar_boleta()
                case 6:
                    break
    def mostrar_funciones_sala(self):
        #santiago acevedo 04/7/2025
        """Este método se encarga de mostrar las funciones de una sala dada"""
        self.mostrar_salas_disponibles()
        try:
            id_sala=int(input("Introduce el id de la sala que deseas consultar: "))
            busqueda_sala=self.buscar_sala(id_sala)
            if busqueda_sala!=-1:
                for funcion in self.salas[busqueda_sala].programacion:
                    if funcion is not None:
                        print(f"Película: {funcion.pelicula.nombre_es} - Fecha: {funcion.fecha.date()} - Hora Inicio: {funcion.hora_inicio.strftime('%H:%M')} - Hora Fin: {funcion.hora_fin.strftime('%H:%M')}")
            else:
                print("Sala no encontrada.")
        except ValueError:
            print("ID de sala inválido. Por favor, introduce un número entero: ")
#Jesica Estor 4/07/2025
    def mostrar_menu_vendedor(self):
        """ESte método se encarga de mostrar el menú del vendedor."""
        opcion=0
        while opcion!=3:
            print("\n%% MENÚ DE OPCIONES VENDEDOR %%\n")
            print("1. Crear cliente\n2. Salir")
            try:
                opcion=int(input("Introduce la opcion que deseas: "))
                match(opcion):
                    case 1:
                        self.registrar_usuario()
                    case 2:
                        break
            except ValueError:
                print("Entrada inválida. Por favor, introduce un número entero: ")
#Mateo Ursuga 2/07/2025        

    def buscar_pelicula(self, id):
        for i in range(self.n_peliculas):
            if self.peliculas[i].id==id:
                return i
        return -1

    def buscar_sala(self, id):
        for i in range(self.n_salas):
            if self.salas[i].id==id:
                return i
        return -1 
#Mateo Ursuga 1/07/2025        

    def mostrar_salas_disponibles(self):
        print("\n%% SALAS DISPONIBLES %%\n")
        contador=1
        for i in range(self.n_salas):
            print("SALA #",contador, " - ID: ", self.salas[i].id," - Número de boletas vendidas: ", self.salas[i].boletas_vendidas, " - Valor de la boleta: ", self.salas[i].valor_boleta)
            contador+=1
#Mateo Ursuga 1/07/2025        

    def modificar_funcion(self):
        """Este método se encarga de modificar una función de una sala dada."""
        self.mostrar_salas_disponibles()
        try:
            id_sala=int(input("Introduce el id de la sala que deseas modificar: "))
            busqueda_sala=self.buscar_sala(id_sala)
            if busqueda_sala!=-1:
                self.salas[busqueda_sala].buscar_funcion(id_sala)
                try:
                    id_funcion=int(input("Introduce el id de la función que deseas modificar: "))
                    funcion=self.salas[busqueda_sala].buscar_funcion(id_funcion)
                    if funcion!=-1:
                        nueva_funcion=Funcion()
                        nueva_funcion.pedir_datos()
                        self.salas[busqueda_sala].programacion[funcion]=nueva_funcion
                        print("Función modificada correctamente.")
                    else:
                        print("Función no encontrada.")
                except ValueError:
                    print("ID de función inválido. Por favor, introduce un número entero: ")
            else:
                print("Sala no encontrada.")
        except ValueError:
            print("ID de sala inválido. Por favor, introduce un número entero: ")
#Mateo Ursuga 2/07/2025        
    
    def annadir_pelicula_funcion(self):
        self.mostrar_salas_disponibles()
        try:
            id_sala=int(input("Introduce el id de la sala que deseas: "))
            busqueda_sala=self.buscar_sala(id_sala)
            if busqueda_sala!=-1:
                self.mostrar_peliculas_activas()
                try:
                    id_pelicula=int(input("Introduce el id de la pelicula que quieres agregar: "))
                    busqueda_pelicula=self.buscar_pelicula(id_pelicula)
                    if busqueda_pelicula!=-1:
                        funcion=Funcion()
                        funcion.pedir_datos()
                        funcion.pelicula=self.peliculas[busqueda_pelicula]
                        funcion.hora_fin=funcion.hora_inicio + timedelta(minutes=funcion.pelicula.duracion)
                        funcion.matriz_asientos=np.full((self.salas[busqueda_sala].filas, self.salas[busqueda_sala].sillas_fila), fill_value=0, dtype=int)
                        if self.verificar_funcion(funcion, self.salas[busqueda_sala]):
                            self.salas[busqueda_sala].set_funcion_programacion(funcion)
                        else:
                            print(f"¡¡Error!! Traslape con '{self.peliculas[busqueda_pelicula].nombre_es}' en sala {self.salas[busqueda_sala].id}.")
                    else:
                        print("Pelicula no encontrada.")
                except:
                    print("Ingresa un valor numerico.")
            else:
                print("Sala no encontrada")
        except:
            print("Ingresa un valor numerico.")
       

    def reservar_boleta(self):
        """Este método se encarga de reservar una boleta para una película en una sala específica"""
        #  santiago acevedo 04/7/2025 
        self.consultar_programacion_pelicula()

        id_sala = int(input("Introduce el id de la sala que deseas: "))
        id_pelicula = int(input("Introduce el id de la película que deseas: "))

        for sala in self.salas:
            if sala.id == id_sala:
                for funcion in sala.programacion:
                    if funcion.pelicula.id == id_pelicula:
                        # Mostrar asientos disponibles (0 = libre, 1 = reservado)
                        print("Asientos disponibles (0 = libre, 1 = reservado):")
                        print(funcion.matriz_asientos)

                        fila = int(input("Introduce la fila que deseas reservar: ")) - 1
                        lista_asientos_reservados = []
                        cantidad_asientos = 0

                        while True:
                            silla = int(input("Introduce el número de silla que deseas reservar: ")) - 1
                            if 0 <= fila < funcion.matriz_asientos.shape[0] and 0 <= silla < funcion.matriz_asientos.shape[1]:
                                if funcion.matriz_asientos[fila][silla] == 0:
                                    funcion.matriz_asientos[fila][silla] = 1
                                    lista_asientos_reservados.append((fila + 1, silla + 1))  
                                    cantidad_asientos += 1
                                    sala.boletas_vendidas += 1  
                                    print("Boleta reservada con éxito.")
                                else:
                                    print("La boleta ya está reservada.")
                            else:
                                print("Fila o silla fuera de rango.")

                            n = input("¿Deseas reservar otra boleta? (1.Sí / 2.No): ")
                            if n != "1":
                                break


                    
                        self.guardar_datos()

                    print(f"**** BOLETA *****\nSala: {sala.id}\nPelícula: {funcion.pelicula.nombre_es}\nFecha: {date.today()}\nAsientos reservados: {lista_asientos_reservados}\nTotal: ${cantidad_asientos * sala.valor_boleta}**** FIN BOLETA *****")
                    return  # Salimos después de reservar
        print("No se encontró la sala o película indicada.")
        
#Mateo Ursuga 2/07/2025        

    def verificar_funcion(self, funcion, sala):
        for i in range(sala.n_funciones):
            if sala.programacion[i].fecha==funcion.fecha and sala.programacion[i].hora_inicio==funcion.hora_inicio:
#                if (funcion.hora_fin <= funcion.hora_inicio or funcion.hora_inicio >= funcion.hora_fin):
                return False
        return True

#Mateo Ursuga 2/07/2025        

    def mostrar_funciones(self):
        if self.n_salas == 0:
            print("No hay funciones programadas.")
            return

        for i in range(self.n_salas):
            for j in range(self.salas[i].n_funciones):
                print(f"Sala {self.salas[i].id} -- {self.salas[i].programacion[j].pelicula.nombre_es}: {self.salas[i].programacion[j].hora_inicio} - {self.salas[i].programacion[j].hora_fin}")
   
#Mateo Ursuga 2/07/2025        

    def mostrar_funcion_sala(self):
        """Este método se encarga de mostrar las funciones de una sala dada."""
        self.mostrar_salas_disponibles()
        try:
            op=int(input("Introduce el id de la sala que quieres ver: "))    
            b=self.buscar_sala(op)
            if b!=-1:
                for i in range(self.salas[b].n_funciones):
                    print(self.salas[b].programacion[i].pelicula.nombre_es)
        except:
            print("Ingrese un valor numerico.")
#Mateo Ursuga 2/07/2025        

    def eliminar_funcion_sala(self):
        """Este método se encarga de eliminar una función de una sala dada."""
        self.mostrar_salas_disponibles()
        try:
            op=int(input("Introduce el id de la sala que quieres ver: "))    
            b=self.buscar_sala(op)
            if b!=-1:
                for i in range(self.salas[b].n_funciones):
                    print("Nombre: ",self.salas[b].programacion[i].pelicula.nombre_es, " - ID: ", self.salas[b].programacion[i].pelicula.id)
            op_e=int(input("Introduce el id de la pelicula que deseas eliminar: "))
            p=self.salas[b].buscar_funcion(op_e)
            if p!=-1:
                for _ in range(self.salas[b].n_funciones-1):
                    self.salas[b].programacion[p]=self.salas[b].programacion[p+1]
                self.salas[b].programacion[self.salas[b].n_funciones-1]=None
                self.salas[b].n_funciones-=1
                print("Se elimino correctamente")
                return True
            return False
        except:
            print("Ingrese un valor numerico.")

    def crear_sala(self):
        nueva_sala=Sala()
        nueva_sala.pedir_datos()
        for i in range(self.n_salas):
            while self.salas[i].id==nueva_sala.id:
                print("Sala con ID existente.")
                nueva_sala.pedir_datos()
        self.salas[self.n_salas]=nueva_sala
        self.n_salas+=1
        self.guardar_datos()
#Jesica Estor 30/06/2025
    def procesar(self):
        op=0

        while op!=3:
            print ("\n%% MENÚ DE APLICACIÓN %%\n")
            print("1. Registrarse \n2. Auntenticarse \n3. Salir de la app")
            try:
                op=int(input("Seleccione una opción del menú: "))
                if op<1 or op>3:
                        print("Opción no válida. Por favor, introduce un número entre 1 y 3.")
                match(op):
                    case 1:
                        self.registrar_usuario()
                    case 2:
                        if self.autenticar_usuario():
                            if self.usuario_autenticado.tipo==Usuario.PERFIL_ADMIN:
                                self.mostrar_menu_admin()
                            elif self.usuario_autenticado.tipo==Usuario.PERFIL_CLIENTE:
                                self.mostrar_menu_cliente()
                            elif self.usuario_autenticado.tipo==Usuario.PERFIL_VENDEDOR:
                                self.mostrar_menu_vendedor()
                    case 3:
                        self.usuario_autenticado=None
                        print("Aplicación terminada")
            except:
                print("Ingresa un dato válido.")
    def guardar_datos(self):
        #santiago acevedo 05/7/2025 5
        """Guarda usuarios, salas y películas en archivos pickle"""
        with open("usuarios1.pkl", "wb") as f:
            pickle.dump(self.usuarios[:self.n_usuarios], f)
        with open("salas1.pkl", "wb") as f:
            pickle.dump(self.salas[:self.n_salas], f)
        with open("peliculas1.pkl", "wb") as f:
            pickle.dump(self.peliculas[:self.n_peliculas], f)

    def cargar_datos(self):
        """Carga usuarios, salas y películas desde archivos pickle si existen"""
        #santiago acevedo 05/7/2025 
        import os
        if os.path.exists("usuarios1.pkl"):
            with open("usuarios1.pkl", "rb") as f:
                usuarios_cargados = pickle.load(f)
                for i, usuario in enumerate(usuarios_cargados):
                    self.usuarios[i] = usuario
                self.n_usuarios = len(usuarios_cargados)

        if os.path.exists("salas1.pkl"):
            with open("salas1.pkl", "rb") as f:
                salas_cargadas = pickle.load(f)
                for i, sala in enumerate(salas_cargadas):
                    self.salas[i] = sala
                self.n_salas = len(salas_cargadas)

        if os.path.exists("peliculas1.pkl"):
            with open("peliculas1.pkl", "rb") as f:
                peliculas_cargadas = pickle.load(f)
                for i, pelicula in enumerate(peliculas_cargadas):
                    self.peliculas[i] = pelicula
                self.n_peliculas = len(peliculas_cargadas)


def main():
    app = AppCine()
    app.cargar_datos()
    app.procesar()
    # al salir:
    app.guardar_datos()
if __name__ == "__main__":
    main()

class Usuario():
    def __init__(self, nombre_usuario, contraseña):
        self.__nombre_usuario = nombre_usuario
        self.__contraseña = contraseña

    @property
    def dar_alta(self):
        pass

    @property
    def iniciar_sesion(self):
        pass

    @property
    def cerrar_sesion(self):
        pass

    @property
    def modificar_nombre(self,nombre_usuario):
        self.__nombre_usuario = nombre_usuario

    @property
    def modificar_contraseña(self,contraseña):
        self.__contraseña = contraseña

    @property
    def dar_baja(self):
        pass

class Receta():
    def __init__(self, nombre, dificultad, ingredientes, tiempo_preparacion):
        self.__nombre = nombre
        self.__dificultad = dificultad
        self.__ingredientes = ingredientes
        self.__tiempo_preparacion = tiempo_preparacion

    @property
    def crear(self):
        pass

    @property
    def modificar_nombre(self,nombre):
        self.__nombre = nombre

    @property
    def consultar(self):
        return f"{self.__nombre} {self.__dificultad} {self.__ingredientes} {self.__tiempo_preparacion}"

    @property
    def eliminar(self):
        pass

    @property
    def apto_vegano(self):
        pass

    @property
    def apto_celíaco(self):
        pass

class Ingrediente():
    def __init__(self, nombre, cantidad):
        self.__nombre = nombre
        self.__cantidad = cantidad

    @property
    def agregar(self):
        pass

    @property
    def consultar(self):
        return f"{self.__nombre} {self.__cantidad}"

class Cantidad():
    def __init__(self, cantidad, unidad_medida):
        self.__cantidad = cantidad
        self.__unidad_medida = unidad_medida

    @property
    def agregar(self):
        pass
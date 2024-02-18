class Asiento:
    def  __init__(self,color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if(color == "rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco"):
            self.color = color


class Motor:
    registro = ""
    def __init__(self,numeroCilindros,tipo,regis):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = regis

    def cambiarRegistro(self,registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        if(tipo == "gasolina" or tipo == "electrico"):
            self.tipo = tipo

class Auto:

    def __init__(self,modelo,precio,marca,asientos,registro,cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        self.asientos = []
        self.registro = registro
        self.cantidadCreados = cantidadCreados


    def cantidadAsientos(self):
        objetos = 0
        for i in self.asientos:
            if i != None :
                objetos = objetos + 1
        return objetos
    
    @classmethod
    def verificarIntegridad(cls):
        if Motor.registro == cls.registro :
            for x in cls.asientos:
                if x != None:
                    if x.registro != Motor.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"








        

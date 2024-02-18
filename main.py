class Asiento:
    color = None
    precio = None
    registro = None

    def cambiarColor(self, color):
        if(color == "rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco"):
            self.color = color


class Motor:
    numeroCilindros = None
    tipo = None
    registro = None

    def cambioRegistro(self,registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        if(tipo == "gasolina" or tipo == "electrico"):
            self.tipo = tipo

class Auto:
    modelo = None
    precio = None
    marca = None
    asientos = []
    registro = None
    cantidadCreados = None


    def cantidadAsientos(self):
        objetos = 0
        for i in self.asientos:
            if i != None :
                objetos = objetos + 1
        return objetos

    def verificarIntegridad(self):
        if Motor.registro == self.registro :
            for x in self.asientos:
                if x != None:
                    if x.registro != Motor.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"


x = Auto()
n1 = Asiento()
n2 = Asiento()

x.asientos.append(n1)
x.asientos.append(n2)
print(x.verificarIntegridad())         



        

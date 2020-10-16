import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 3 numeros
2+4+6 = 12
"""


# start-->
def suma(num1, num2, num3):
    resultado = num1 + num2 + num3
    return resultado


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros impares del 1 al 1000
"""


# start-->
def sumaImpares():
    result = 0
    for numero in range(1, 1001, 2):
        result = result + numero
    print(result)




"""
***************************************************************
@@ ejercicio 3 @@
encontrar el perimetro, area y el volumen de un esfera
radio = 12 m

perimetro: 2*pi*r
area: 4*pi*r^2
volumen: (4/3)*pi*r^3
"""


# start-->
def definicionEsfera(radio):
    return radio


def obtenerPerimetro(radio):
    self.radio = radio
    result = 2 * 3.1415926535897932384 * radio
    return result


def obtenerArea(radio):
    result = 4* 3.1415926535897932384*radio^2
    return result


def obtenerVolumen(radio):
    result = (4/3)*3.1415926535897932384*radio^3
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Esfera:
    def __init__(self, radio):
        self.radio = radio

    def ObtenerPerimetro(self):
        radio = self.radio
        perimetro = 2 * 3.1415926535897932384 * radio
        print(perimetro)
        
    def obtenerArea(self):
        radio = self.radio
        area = 4 * 3.1415926535897932384 * radio^2
        return area

    def obtenerVolumen(self):
        radio = self.radio
        volumen = (4 / 3) * 3.1415926535897932384 * radio^3
        return volumen



"""
***************************************************************
@@ ejercicio 5 @@
Banco
Cliente
    nombre
    lugar
    numero de cuenta
    transaccion - retiro o abono
    monto
"""


class Banco:
    def __init__(self, nombre, lugar, numCuenta, tipoRetiro, monto):
        self.nombre = nombre
        self.monto = monto

    def procesar(self):
        return 0

    def abonosSanSalvador(self):
        if Cliente.transaccion == "abono":
            cantidadAbonos = Cliente.transaccion
        return cantidadAbonos

    def abonosBalYRod(self):
        return 0


class Cliente:
    def __init__(self, nombre, lugar, numCuenta, transaccion, monto):
        self.nombre = nombre
        self.lugar = lugar
        self.numCuenta = numCuenta
        self.transaccion = transaccion
        self.monto = monto


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return ""

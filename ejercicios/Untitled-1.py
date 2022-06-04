class Empresa:

    def __init__(self, nombre, ingresos, egresos):
        self.nombre = nombre
        self.ingresos = ingresos
        self.egresos = egresos

    def calcularGanancias(self):
        ganancia = self.ingresos - self.egresos
        return ganancia

salida = True
while (salida == True):
    print("Ingrese el nombre de la empresa")
    nombre = input()
    print("Ingrese los ingresos de la empresa")
    ingresos = float(input())
    print("Ingrese los egresos de la empresa")
    egresos = float(input())
    empresa = Empresa(nombre, ingresos, egresos)
    print("Ganancias de la empresa: " + empresa.calcularGanancias())


    print("Desea seguir ingresando empresas?")
    salida = input()
    if(salida == "no"):
        salida = False
    else:
        salida = True

class Propietarios:

    def __init__(self, nombre, direccion,numero):
        self.nombre = nombre
        self.departamento = (str(direccion)+str(numero))
    def obtenerPropietario(self):
        propietario = ("Dato ingresado: \n" + self.nombre + "-" + "-" + self.departamento + "\n")
        return propietario

salida = True
while (salida == True):
    print("Ingrese el nombre del dueno del departamento")
    nombre = input()
    print("Ingrese la direccion del apartamento")
    direccion= input()
    print("Ingrese el numero de departamento")
    numero = int(input())


    propietario = Propietarios(nombre, direccion,numero)
    print("Desea seguir ingresando departamentos?")
    salida = input()
    if(salida == "no"):
        salida = False
        print(propietario.obtenerPropietario())
    else:
        salida = True
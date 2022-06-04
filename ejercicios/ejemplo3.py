class Calificaciones:

    def __init__(self, nombre, nota, nota2):
        self.nombre = nombre
        self.nota = nota
        self.nota2 = nota2

    def calcularpromedio(self):
        promedio = (self.nota + self.nota2) / 2
        return promedio

salida = True
while (salida == True):
    print("Ingrese el nombre del estudiante")
    nombre = input()
    print("Ingrese la primera nota del estudiante")
    nota = float(input())
    print("Ingrese la segunda nota del estudiante")
    nota2 = float(input())
    estudiante = Calificaciones(nombre, nota, nota2)
    print("promedio del estudiante: " + estudiante.calcularpromedio())


    print("Desea seguir ingresando alumnos con sus notas?")
    salida = input()
    if(salida == "no"):
        salida = False
    else:
        salida = True





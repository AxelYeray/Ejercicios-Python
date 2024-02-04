# Escribir la funcion Max

# Esta funcion toma dos numeros y los compara
# para ver cual es el mayor de estos dos


def funcion_max(n1, n2):
    if n1 > n2:
        print("El numero mayor es: ", n1)
        return n1
    else:
        print("El numero mayor es: ", n2)
        return n2


a = int(input("ingrese el primer numero: "))
b = int(input("ingrese el segundo numero numero: "))


print(funcion_max(a, b))

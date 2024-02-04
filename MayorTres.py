# Escribir una funcion max para tres numeros


def funcion_maxtres(n1, n2, n3):
    """Esta funcion toma tres numeros y verifica el mayor"""
    if n1 > n2 and n1 > n3:
        return n1

    elif n2 > n1 and n2 > n3:
        return n2

    else:
        return n3


a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

print(funcion_maxtres(a, b, c))

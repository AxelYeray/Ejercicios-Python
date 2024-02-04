# Ingresar una cadena en invertirla


def inversion(palabra):
    reversa = palabra[::-1]
    return reversa


a = input("Ingresa una palabra: ")

print(inversion(a))

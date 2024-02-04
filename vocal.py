# Escribir una función que tome un carácter y devuelva True si es una vocal,
# de lo contrario devuelve False


def vocalono(n):
    return True if n in "aeiou" else False


a = input("Ingrese un caracter: ")

print(vocalono(a))

# Escribir la funcion len por nuestra cuenta


def len2(palabra):
    """Esta es la funcion len programada por mi"""
    x = 0
    for i in palabra:
        x = x + 1

    return x


cadena = input("Ingrese una palabra: ")


print(len2(cadena))

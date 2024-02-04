# Definir una función superposicion() que tome dos listas y devuelva True
# si tienen al menos 1 miembro en común o devuelva False de lo contrario.
# Escribir la función usando el bucle for anidado.


def superposicion(n1, n2):
    for elemento1 in n1:
        for elemento2 in n2:
            if elemento1 == elemento2:
                return True
    return False


# Ejemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 1]

resultado = superposicion(lista1, lista2)
print(resultado)

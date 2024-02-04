# Escribir una función sum() y una función multip() que sumen y multipliquen
# respectivamente todos los números de una lista.
# Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24


def suma(listas):
    x = 0
    for i in listas:
        x = x + i

    return x


def multip(listas):
    x = 0
    for i in listas:
        x = x * i

    return x


lista = [1, 2, 3, 4, 5]

print(suma(lista))
print(multip(lista))

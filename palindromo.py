# Escriba un programa que verifique si una palabra es una palindromo o no


def palindromo(palabra):
    reversa = palabra[::-1]
    if reversa == palabra:
        return "Es un palindromo"
    else:
        return "No es palindromo"


a = input("Ingresa una palabra: ")

print(palindromo(a))

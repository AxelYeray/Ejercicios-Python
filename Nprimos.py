# Determinar si un número es primo o no

n = int(input("Ingrese un nùmero:"))
c = 0
i = 1

while i <= n:
    if n % i == 0:
        c = c + 1
    i = i + 1
if c == 2:
    print("El número", n, "es primo")
    print(2 % 1)
else:
    print("El número", n, "no es primo")

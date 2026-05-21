numeros = []

for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

print("Números na ordem inversa:")

for numero in reversed(numeros):
    print(numero)
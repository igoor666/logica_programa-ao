numeros = []
pares = []
impares = []

for i in range(20):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Vetor completo:")
print(numeros)

print("Vetor pares:")
print(pares)

print("Vetor ímpares:")
print(impares)
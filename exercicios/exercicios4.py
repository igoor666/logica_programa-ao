caracteres = []
consoantes = []

# lendo 10 caracteres
for i in range(10):
    letra = input(f"Digite o {i+1}º caractere: ").lower()
    caracteres.append(letra)

    # verificando se é consoante
    if letra.isalpha() and letra not in "aeiou":
        consoantes.append(letra)

# mostrando resultado
print(f"Foram lidas {len(consoantes)} consoantes")

print("Consoantes digitadas:")
for letra in consoantes:
    print(letra)

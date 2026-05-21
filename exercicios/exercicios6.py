medias = []
aprovados = 0

# lendo as notas de 10 alunos
for i in range(10):
    print(f"\nAluno {i+1}")

    soma = 0

    # lendo as 4 notas
    for j in range(4):
        nota = float(input(f"Digite a {j+1}ª nota: "))
        soma += nota

    # calculando média
    media = soma / 4
    medias.append(media)

    # verificando aprovados
    if media >= 7:
        aprovados += 1

# mostrando resultados
print("\nMédias dos alunos:")
print(medias)

print(f"Quantidade de alunos com média maior ou igual a 7: {aprovados}")
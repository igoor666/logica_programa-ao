# pedir # notas e armazenar em variaveis diferentes

nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))

# calcular a media
soma = nota1 + nota2 + nota3
media = soma / 3
# mostrar a media
print("A média das notas é: ", media)
if media >= 7:
    print("Parabéns, você foi aprovado!")
    print("continue assim vc e bom ")
else:
    if media >= 4:
        print("você ficou de recuperação")
        print("estuda mais seu raparigo safado")      
    else: 
        print("Infelizmente, você foi reprovado.")
        print("estuda mais seu raparigo safado")
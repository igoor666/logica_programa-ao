# nesse codigo, analisaremos a idade e falaremos
# se e maior de idade ou nao 
nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))

print("ola, ", nome, "! a sua idade: ", idade )

# a  estrutura de deciçao analisa uma comparaçao e executar o codigo
# com base na resposta. para utilizarmos a estrutura de decisao, precisamos
# de comparadores , que sao: 
# 
# -> maior
# -< menor 
# -== igual
# -!= diferente
# ->= maior ou igual
# -<= menor ou igual
# - ! nao

# O comando de decisao e o if
#A sintaxe é:
# if comparaçao 
#E os itens a seram executados devem estar em um bloco identado.
# if 20 > 30:
#    print("algo de errado nao esta certo")

if idade > 18:
    print("voce e maior de idade")
    if idade >= 60:
        print("voce e idoso")
        print("Já pode pegar a carteirinha de estacionamento")
else:
    print("voce e menor de idade")
    print(" Nâo pode comprar cigarro no Reino Unido")
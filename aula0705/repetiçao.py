import time
import random

print("#### jogo de adivinhaçao")
print()
print("estou pensando em um numero")

time.sleep(2)

numero = random.randint(0,10)

print("pensei")
print("voce podera tentar adivinhar ele")
print()
# para i em um intervalo de 1 ate 4
#for i in range(1,4):
#    print(f"essa e a sua {i} tentativa!")
   # tentativa = int(input("digite um valor entre 0 e 10 : "))

#if tentativa == numero:
  #  print("parabens voce acertou!")
#else:
  # print("voce errou")

acertou = False
num_tentativa = 0
while acertou == False:
    num_tentativa += 1 # MESMA COISA QUE  NUM_ TENTATIVA = num_tentativa + 1
    print(f"essa e a {num_tentativa} tentativa")
    tentativa = int(input("digite um valor entre 0 e 10: "))

    if tentativa  == numero:
        print("parabens voce acertou!")
        acertou = True
     
    else:
        print("voce errou")
        if num_tentativa == 10:
            print("para de ser toiso raparigo safado")

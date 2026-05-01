from unittest import case


print("|----------------------|")
print("|     CALCULADORA      |")
print("|----------------------|")
print()
print("essa calculadora, faz todas as operações")
print("a partir de dois numeros que voce informar")
print()

print("digite o valor correspomdente ao calculo")
print(" que voce deseja fazer: ")
print()
print("1 - as 4 operações basicas")
print("2 - media de 3 valores")
print("3 - formaula de bhaskara")
print()
opcao = int(input("digite a opção: "))

match opcao:
    case 1:
        first_number = float(input("digite o primeiro numero: "))
        second_number = float(input("digite o segundo numero: "))
        print()

        adicao = first_number + second_number
        print(f"o resultado da adição é {adicao}")

        subtracao = first_number - second_number
        print(f"o resultado da subtração é {subtracao}")

        multiplicacao = first_number * second_number
        print(f"o resultado da multiplicação é {multiplicacao}")

        # verificar se o segundo numero é diferente de 0
        if second_number != 0:
            divisao = first_number / second_number
            print(f"o resultado da divisão é {divisao}")
        else:
            print("não é possível dividir por zero")   

    case 2: 
        print("media de 3 valores")
        nota1 = float(input("digite a primeira nota: "))
        nota2 = float(input("digite a segunda nota: "))
        nota3 = float(input("digite a terceira nota: "))

        soma = nota1 + nota2 + nota3
        media = soma / 3

        print(f"A média das notas é: {media}")
        if media >= 7:
            print("Parabéns, você foi aprovado!")
            print("continue assim vc e bom ")
        else:
            if media >= 4:
                print("você ficou de recuperação")     
            else: 
                print("Infelizmente, você foi reprovado.")

    case 3:
                print("fórmula de bhaskara")
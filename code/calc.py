from ast import While
from time import sleep
from tkinter import N


print("\n \t Bem vindo! \n")
nome = input("Digite seu nome: ")

print('Olá,',nome, "\nCalcule qualquer coisa comigo :)\n")

while True:
    print('Escolha uma das opções')
    inicio = float(input("Para somar: '1'\n"
                    "Para subtrair: '2'\n"
                    "Para dividir: '3'\n"
                    "Para multiplicar: '4'\n"
                    "Para calular raiz quadrada: '5'\n"
                    "Para calcular potenciação de números: '6'\n"
                    "Para calcular funções trigonométricas: '7'\n"
                    "Para fechar o programa: 'n'\n"))





    if inicio == 'n':
        print("\tObrigado por usar esta calculadora!\n\tAté breve :D")
        exit()

    import math

    if inicio == '1':
        print("\tOpção escolhida: 'Soma'\n")

        primeiro = float(input('Digite o primeiro número: '))
        segundo = float(input('Digite o segundo número: '))

        conta = float(primeiro) + float(segundo)

        print(f'\nO resultado das somas é {conta:,.0f}\n\n')

        sleep(4)

    if inicio == '2':
        print("\tOpção escolhida: 'Subtração'\n")

        primeiro = float(input('Digite o primeiro número: '))
        segundo = float(input('Digite o segundo número: '))

        conta = float(primeiro) - float(segundo)

        print(f'\nO resultado da subtração é {conta:,.0f}\n\n')

        sleep(4)

    if inicio == '3':
        print("\tOpção escolhida: 'Divisão'\n")

        primeiro = float(input('Digite o primeiro número: '))
        segundo = float(input('Digite o segundo número: '))

        conta = float(primeiro) / float(segundo)

        print(f'\nO resultado da divisão é {conta:,.1f}\n\n')


        sleep(4)
    
    if inicio == '4':
        print("\tOpção escolhida: 'Multiplicação'\n")

        primeiro = float(input('Digite o primeiro número: '))
        segundo = float(input('Digite o segundo número: '))

        conta = float(primeiro) * float(segundo)

        print(f'\nO resultado da multiplicação é {conta:,.1f}\n\n')

        sleep(4)

    
    if inicio == '5':
        import math
        
        print("\tOpção escolhida: 'Raiz quadrada'\n")

        numero = float(input('Digite um número: '))
        raiz = math.sqrt(numero)
        print(f'\nO resultado da raiz quadrada é {raiz:,.1f}\n\n')

        sleep(4)

    
    if inicio == '6':
        import math

        print("\tOpção escolhida: 'Potenciação de números'\n")

        primeiro = float(input('Digite o primeiro número: '))
        elevado = float(input('Digite o número elevado: '))
        poten = math.pow(primeiro, elevado)

        print(f'\nO resultado da potência é {poten:,.1f}\n\n')

        sleep(4)
    break

while inicio:
    if inicio == '7':
        print("\tOpção escolhida: 'Funções trigonométricas'\n")
            
        print("Escolha uma das opções:")
        trigon  = (input("Para calcular seno: '1'\n"
                   "Para calcular cosseno: '2'\n"
                   "Para calcular tangente: '3'\n"
                   "Para cancelar esta ação: 'n'\n"))

        


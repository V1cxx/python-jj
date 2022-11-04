from tkinter import N


print("\n \t Bem vindo! \n")
nome = input("Digite seu nome: ")

print('Olá,',nome, "\nCalcule qualquer coisa comigo :)\n")

while True:
    print('Escolha uma das opções')
    inicio = input("Para somar: '1'\n"
                    "Para subtrair: '2'\n"
                    "Para dividir: '3'\n"
                    "Para multiplicar: '4'\n"
                    "Para calular raiz quadrada: '5'\n"
                    "Para calcular potenciação de números: '6'\n"
                    "Para calcular funções trigonométricas: '7'\n"
                    "Para fechar o programa: 'n'\n")





    if inicio == 'n':
        print("\tObrigado por usar esta calculadora!\n\tAté breve :D")
        exit()


    if inicio == '1':
        print("Opção escolhida: 'Soma' ")

        primeiro = input('Digite o primeiro número: ')
        segundo = input('Digite o segundo número: ')

        conta = float(primeiro) + float(segundo)

        print('O resultado das somas é',conta.__format__(conta))

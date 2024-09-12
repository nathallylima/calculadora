print("\n Calculadora")

while True:
    opcao = float(input("\n Digita a opção que deseja: \n 1 - Soma \n 2 - Subtração \n 3 - Divisão \n 4 - Multiplicação \n 5 - Sair \n"))

    if opcao == 1:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        resultado = n1 + n2
        print(f'Soma: {n1} + {n2} = {resultado}')
    elif opcao == 2:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        resultado = n1 - n2
        print(f'Subtração: {n1} - {n2} = {resultado}')
    elif opcao == 3:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        resultado = n1 / n2
        print(f'Divisão: {n1} / {n2} = {resultado}')
    elif opcao == 4:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        resultado = n1 * n2
        print(f'Multiplicação: {n1} x {n2} = {resultado}')
    elif opcao == 5:
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Digite o número correspondente à opção desejada.")

        
        
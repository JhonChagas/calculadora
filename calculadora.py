def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

# Função principal
def calculadora():
    while True:
        print("Selecione a operação:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")

        opcao = input("Digite o número da operação desejada: ")

        if opcao == "5":
            print("Calculadora encerrada.")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = somar(num1, num2)
        elif opcao == "2":
            resultado = subtrair(num1, num2)
        elif opcao == "3":
            resultado = multiplicar(num1, num2)
        elif opcao == "4":
            resultado = dividir(num1, num2)
        else:
            print("Opção inválida!")
            continue

        print("Resultado: ", resultado)
        print()

# Execução da calculadora
calculadora()


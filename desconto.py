def soma(number, number2):
    resultado = number + number2
    return resultado

def subtracao(num, num2):
    resultado = num - num2
    return resultado

def multiplicacao(num1, num2):
    resultado = num1 * num2
    return resultado

def divisao(num1, num2):
    resultado = num1 / num2
    return resultado

opcao = -1

while opcao != 0:
    try:

        print("Escolha uma opção:")
        opcao = int(input("1 - Soma\n" "2 - Subtração\n" "3 - Multiplicação\n" "4 - Divisão\n" "0 - Sair"))

        if opcao == 1:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Agora o segundo: "))

            resultado = soma(num1, num2)

            print(f"O resultado é {resultado}")

        elif opcao == 2:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Agora o segundo: "))
            
            resultado = subtracao(num1, num2)
            
            print(f"O resultado é {resultado}")

        elif opcao == 3:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Agora o segundo: "))
            
            resultado = multiplicacao(num1, num2)
            
            print(f"O resultado é {resultado}")

        elif opcao == 4:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Agora o segundo: "))
            
            resultado = divisao(num1, num2)
            
            print(f"O resultado é {resultado}")

        elif opcao != 0:
            print("Digite algo válido por favor")


    except ValueError:
        print("Digite apenas números por favor")
    except ZeroDivisionError:
        print("Não é possível dividir por zero.")

print("Fim.")

        

        


    
    
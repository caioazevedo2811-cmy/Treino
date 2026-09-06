saldo = 1000
opcao = -1

while opcao != 0:
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("0 - Sair")

    opcao = int(input("Selecione uma opção "))

    if opcao == 1:
        print("Seu saldo atual é R$" , saldo)

    elif opcao == 2:
        deposito = float(input("Qual valor você deseja depositar? "))

        saldo = saldo + deposito

    elif opcao == 3:
        saque = float(input("Qual valor você deseja sacar? "))

        if saque > saldo:
            print("Saldo insuficiente")

        else:
            print("Saque realizado.")
            saldo = saldo - saque

    elif opcao != 0:
        print("Opção inválida.")

print ("Programa encerrado.")


        


        




import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()
time.sleep(0.1)


def estacionar(horas):
    if horas <= 1 and horas > 0:
        valor = 8

    elif horas <=3:
        valor = 15

    elif horas > 3:
        valor = 20

    return valor

quantidade = 0
total = 0
horas = -1

while horas != 0:
    try:

        while horas < 0:

            horas = float(input("Informe quantas horas o veículo ficou (0 para encerrar): "))

            if horas < 0:
                print("Informe um valor valído por favor.")

                limpar_tela()
                input("Digite ENTER para continuar: ")

        limpar_tela()

        if horas > 0:

            quantidade += 1

            valor = estacionar(horas)

            total += valor

            print(f"O valor a ser pago é: R${valor:.2f}.")

        horas = float(input("Informe quantas horas o próximo veículo ficou (0 para encerrar): "))

        limpar_tela()

    except ValueError:
        print("Digite um valor válido por favor.")
        input("Digite ENTER para continuar: ")

        limpar_tela()

print("Fim do sistema.")
input("Digite ENTER para continuar: ")

if quantidade > 0:
    media = total / quantidade

    print(f"O total arrecadado hoje foi de: R${total:.2f}.")
    print(f"A quantidade de veículos que estacionaram hoje foi de {quantidade} veículos.") 
    print(f"A média paga por cada veículo foi de: {media:.2f}")

else:
    print("Nenhum veículo estacionou hoje")
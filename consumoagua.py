import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

numeros = []
consumos = []
faturamento = 0
m20 = 0

valido = False

while not valido:
    try:

        numero = int(input("Informe o número do apartamento: ")) 
        valido = True

    except ValueError:
        print("Digite uma opção válida por favor.")
        input("Digite ENTER para continuar: ")

        limpar_tela()

while numero != 0:
    try:

        numeros.append(numero)

        moradores = int(input("Quantas pessoas moram nesse apartamento?: "))

        while moradores <= 0:
            limpar_tela()

            print("Informe valores válidos por favor.")
            input("Digite ENTER para continuar: ")

            moradores = int(input("Quantas pessoas moram nesse apartamento?: "))

            limpar_tela()

        consumo = float(input("Qual foi o consumo de água (Informe em m³)?: "))

        while consumo <= 0:
            limpar_tela()

            print("Digite um valor válido por favor.")
            input("Aperte ENTER para continuar: ")

            consumo = float(input("Qual foi o consumo de água (Informe em m³)?: "))

            limpar_tela()

        consumos.append(consumo)

        if consumo <= 10:
            preco = consumo * 4.50

            faturamento += preco

            print(f"O preço a ser pago é de R${preco:.2f}")
            input("Aperte ENTER para continuar: ")

            limpar_tela()

        elif consumo <= 20:
            preco = consumo * 6

            faturamento += preco

            print(f"O preço a ser pago é de R${preco:.2f}")
            input("Aperte ENTER para continuar: ")

            limpar_tela()

        else:
            preco = consumo * 8.50

            faturamento += preco

            m20 += 1

            print(f"O preço a ser pago é de R${preco:.2f}")
            input("Aperte ENTER para continuar: ")

            limpar_tela()

        valido = False

        while not valido:
            try:
                numero = int(input("Informe o número do apartamento: "))
                valido = True

            except ValueError:
                limpar_tela()

                print("Digite um valor valido por favor.")
                input("Digite ENTER para continuar: ")
                
                limpar_tela()

    except ValueError:
        limpar_tela()

        print("Insira um valor válido por favor.")
        input("Aperte ENTER para continuar: ")

        limpar_tela()

if len(numeros) > 0:

    consumost = sum(consumos)

    media = consumost / len(numeros)

    percentual = (m20 / len(numeros)) * 100

    maior = consumos[0]
    apm = numeros[0]

    for i in range(len(consumos)):
        if consumos[i] > maior:
            maior = consumos[i]
            apm = numeros[i]
    
    print(f"O total de apartamentos cadastrados foi de {len(numeros)} apartamentos.")
    print(f"O consumo total de água foi de {consumost:.2f}.")
    print(f"O valor total arrecadado foi de R${faturamento:.2f}.")
    print(f"A média da quantidade de água consumida pela quantidade de apartamentos foi de {media:.2f}.")
    print(f"O apartamento com o maior consumo foi o apartamento de número {apm}, que consumiu {maior}m³.")
    print(f"A quantidade de apartamentos que consumiram mais de 20m³ de água foi {m20} apartamentos, o que dá um percentual de {percentual:.2f}.")
    input("Digite ENTER para encerrar: ")
else:
    print("Nenhum apartamento foi registrado.")
    input("Digite ENTER para encerrar: ")





            



        


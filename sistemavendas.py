import os
import time

def limpar_tela():

    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()
time.sleep(0.1)

def calculo(quantidade, preco):
    valor = quantidade * preco

    return valor

codigosp = []
codigos = []
vendas = []
quantp = 0
faturamento = 0

codigo = input("Informe seu código de funcionário (0 para encerrar): ")

while codigo != "0":
    try:

        codproduto = input("Informe o código do produto: ")
                
        preco = float(input("Informe o preço unitário do produto: "))

        while preco <= 0:
            print("Digite um valor válido por favor.")
            input("Digite ENTER para continuar: ")

            limpar_tela()

            preco = float(input("Informe o preço unitário do produto: "))
            

        quantidade = int(input("Informe a quantidade de produtos vendidos: "))

        while quantidade <= 0:
            print("Digite um valor válido por favor.")
            input("Digite ENTER para continuar: ")
            
            limpar_tela()

            quantidade = int(input("Informe a quantidade de produtos vendidos: "))
        
        quantp += quantidade

        valor = calculo(quantidade, preco)

        faturamento += valor

        codigos.append(codigo)
          
        codigosp.append(codproduto)

        vendas.append(valor)

        input("Digite ENTER para continuar: ")

        print(f"O preço a ser pago é de R${valor:.2f}.")

        limpar_tela()

        input("Obrigado por registrar a venda, digite ENTER para continuar: ")

        limpar_tela()

        codigo = input("Informe seu código de funcionário (0 para encerrar): ")

    except ValueError:
        limpar_tela()

        print("Digite um valor válido por favor.")
        input("Digite ENTER para continuar: ")

        limpar_tela()

if len(vendas) > 0:
    media = faturamento / len(vendas)
    maior = max(vendas)
    menor = min(vendas)

    for i in range(len(vendas)):
        if vendas[i] == maior:
            maiorvend = codigos[i]

        if vendas[i] == menor:
            menorvend = codigos[i]

else:
    media = 0
    maior = 0
    menor = 0
    maiorvend = 0
    menorvend = 0
    
print(f"O valor total acumulado hoje foi de R${faturamento:.2f}.")
print(f"A quantidade de vendas foi de {len(vendas)}.")
print(f"A quantidade de produtos vendidos foi de {quantp} produtos.")
print(f"A média do faturamento pela quantidade de vendas foi de R${media:.2f}.")
print(f"O valor da maior venda foi de R${maior:.2f}.")
print(f"O valor da menor venda foi de R${menor:.2f}.")
print(f"O vendedor que fez a maior venda foi o de código {maiorvend}.")
print(f"O vendedor que fez a menor venda foi o de código {menorvend}.")

if faturamento > 5000:
    print("Hoje o faturamento foi excelente, ultrapassando a marca de R$5000.")

elif faturamento <= 5000 and faturamento >= 2000:
    print("Hoje o nível de faturamento foi normal.")

else:
    print("Hoje o faturamento foi baixo, com menos de R$2000 acumulados.")

print("Fim do sistema")
input("Digite ENTER para encerrar.")




        

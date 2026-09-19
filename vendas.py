quantidadev = 0
faturamento = 0
m500 = 0
vendas = []

def calculo(quantidade, preco):
    valor = quantidade * preco

    return valor

def meta(valor):
    global m500

    if valor >= 500:
        m500 += 1

preco = float(input("Informe o valor unitário do produto: "))

quantidade = int(input("Informe a quantidade de produtos (0 para sair): "))

while quantidade > 0:
    try:
        valor = calculo(quantidade, preco)

        meta(valor)

        print(f"O valor da compra foi de: {valor:.2f}")

        quantidadev += 1

        faturamento += valor

        vendas.append(valor)

        preco = float(input("Informe o valor unitário do produto: "))

        quantidade = int(input("Informe a quantidade de produtos (0 para sair): "))

    except ValueError:
        print("Digite apenas números válidos por favor.")

if quantidadev == 0:
    print("Nenhuma venda foi realizada.")

else:
    media = faturamento/quantidadev
    mvenda = max(vendas)

    print(f"A quantidade de vendas foi de {quantidadev} vendas.")
    print(f"O faturamento foi de R${faturamento:.2f}")
    print(f"A média das vendas foi de R${media:.2f}.")
    print(f"O valor da maior venda foi de R${mvenda:.2f}.")
    print(f"A quantidade de vendas que alcançaram ou ultrapassaram R$500 foi de {m500} vendas.")

    





faturamento = 0
quantidadet = 0
pedidos = []
quantidadep = 0

codigo = input("Digite o código do produto: ")

while codigo != "0":
    try:
        quantidade = int(input("Quantos produtos foram pedidos? "))
        preco = float(input("Informe o preço unitário: "))
        
        valor = quantidade * preco
        
        faturamento = faturamento + valor
        
        quantidadep = quantidadep + 1
        
        quantidadet = quantidadet + quantidade
        
        pedidos.append(quantidade)
        
        print(f"O valor do pedido foi de: R${valor:.2f}")
        
        codigo = input("Informe o código do próximo produto: ")
        
    except ValueError:
        print("Digite apenas valores válidos por favor.")
        
if quantidadep > 0:
        
    maiorp = max(pedidos)

else:
    maiorp = 0

if faturamento > 3000:
    print(f"Parabéns, hoje o faturamento ultrapassou R$3000, com um total de R${faturamento:.2f} alcançados.")
    
else:
    print(f"Hoje o faturamento foi de R${faturamento}.")
    
print(f"A quantidade de pedidos foi de {quantidadep} pedidos.")
print(f"A quantidade total de itens vendidos foi de {quantidadet} itens.")
print(f"O maior pedido realizado continha {maiorp} itens.")
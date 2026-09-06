quantidade = 0
total = 0
preço = 0

preço = float(input("Informe os valores dos produtos:"))



while preço != 0:
    quantidade = quantidade +1

    total = total + preço

    preço = float(input("Continue informando os valores:"))

if quantidade > 0:
    media = total/quantidade

    print("O valor total é de:" ,total, "reais.")

    print("A média dos valores é de:" , media)

    print("E a quantidade de produtos é:" , quantidade)

else:
    print("Nenhum preço foi informado.")


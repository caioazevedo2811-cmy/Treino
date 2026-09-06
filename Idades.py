quantidade = 0
total = 0

idades = int(input("Informe as idades:"))

while idades != 0:
    quantidade = quantidade +1
    total = total + idades

    idades = int(input("Continue informando as idades:"))


if quantidade > 0:
    media = total/quantidade

    print("A quantidade de pessoas que tiveram suas idades informadas foi de:" ,quantidade, "pessoas.")
    print("A soma das idades é de:" ,total)
    print("E a média é de:" , media)

else:
    print("Nenhuma idade foi informada")
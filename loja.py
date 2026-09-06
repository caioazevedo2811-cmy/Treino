valort = 0
valores = []
func = []
quantidade = 0

cod = int(input("Informe o seu código: "))

while cod != 0:
    try:

        valor = float(input("Informe o valor da venda: "))

        func.append(cod)

        valort = valort + valor
        valores.append(valor)

        quantidade = quantidade + 1

        cod = int(input("Informe o seu código: "))

    except ValueError:
        print("Informe um valor válido")

                                            

if quantidade > 0:
    media = valort / quantidade
    mv = max(valores)

    for i in range(len(valores)):
        if valores[i] == mv:
            func[i] = func[i]

    print(f"O valor total vendido foi de: R${valort}.")
    print(f"A média foi de R${media}.")
    print(f"A quantidade de produtos vendidos foi de: {quantidade}.")
    print(f"O funcionário que fez a maior venda foi o {func[i]}")


else:
   print("Nenhuma venda foi registrada.")

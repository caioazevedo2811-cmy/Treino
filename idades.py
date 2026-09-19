pessoas = []
quantidade = 0
maior = 0
menor = 1000

nome = input('Digite o nome da pessoa ("SAIR" para sair): ')

while nome.upper() != "SAIR":
    try:
        idade = int(input("Informe a idade: "))
        
        while idade > 125 or idade <= 0:
             print("Informe uma idade válida por favor.")
             
             idade = int(input("Informe a idade: "))
             
        cidade = input("Informe a cidade em que ela mora: ")
        
        pessoa = {"nome" : nome, "idade" : idade, "cidade" : cidade}
        
        pessoas.append(pessoa)
        
        quantidade += 1
        
        nome = input("Digite o nome da pessoa: ")
        
    except ValueError:
        print("Digite um valor válido por favor.")
        
if quantidade > 0:
    for pessoa in pessoas:
        if pessoa["idade"] > maior:
            maior = pessoa["idade"]
            
            nomem = pessoa["nome"]
            
        if pessoa["idade"] < menor:
            menor = pessoa["idade"]
            
            nomep = pessoa["nome"]
            
    print(f"A quantidade de pessoas registradas foi de {quantidade} pessoas.")
    print(f"O nome da pessoa mais velha registrada é {nomem}, que tem seus {maior} anos.")
    print(f"O nome da pessoa mais nova registrada é {nomep}, que tem seus {menor} anos.")
            
else:
    print("Nenhuma pessoa foi registrada.")
pessoas = []

while True:
    try:
        nome = input('Digite seu nome ("SAIR" para sair): ')
        
        if nome.upper() == "SAIR":
            print("Programa encerrado.")
            
            break
        
        idade = int(input("Informe sua Idade: "))
        cidade = input("Em que cidade você mora?: ")
        
        pessoa = {"nome" : nome, "idade" : idade, "cidade" : cidade}
        
        pessoas.append(pessoa)
        
        print(*pessoas)
        
    except ValueError:
        print("Valor inválido.")
        

print(f"As pessoas registradas foram: {pessoas}")

while True:
    opcao = input('Deseja procurar alguma pessoa? (Digite "Sim" ou "Não" )')
        
    while opcao.upper() != "SIM" and opcao.upper() != "NÃO":
        print("(Digite apenas Sim ou Não)")
            
        opcao = input("Deseja procurar alguma pessoa?")
        
    if opcao.upper() == "NÃO":
        print("Programa encerrado.")
            
        break
        
    busca = input("Digite o nome da pessoa que você procura: ")
    
    encontrou = False
        
    for pessoa in pessoas:
        if pessoa["nome"].upper() == busca.upper():
            print(pessoa)
            encontrou = True
            
    if encontrou:
        print("Pessoa encontrada!")
        
    else:
        print("Pessoa não registrada.")
                
    
                
print("Fim.")
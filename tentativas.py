tentativas = 0

while tentativas < 3:
    nome=input("Qual é seu nome?")
    senha=input("Qual é sua senha?")

    if senha == "1234":
        print("Login autorizado, seja bem-vindo" , nome)

        break

    else:

        tentativas = tentativas+1

        print("Senha incorreta, você ainda tem" , 3-tentativas, "tentativas")

if tentativas == 3:
    print("Acesso bloqueado.")
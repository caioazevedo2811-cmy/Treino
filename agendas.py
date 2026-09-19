from datetime import datetime, timedelta

consultas = []
proxid = 1

def agendar():
        global proxid
        
        try:


            nome = input("Digite o nome do paciente: ")

            medico = input("Digite o nome do médico: ")

            especialidade = input("Digite a especialidade do médico: ")

            data = input("Digite a data da consulta (dd/mm/aaaa): ")

            hora = input("Digite a hora da consulta (hh:mm): ")

            dataex = f"{data} {hora}"

            dataex = datetime.strptime(dataex, "%d/%m/%Y %H:%M") 

            consulta = {"id": proxid, "nome" : nome, "medico" : medico, "especialidade" : especialidade, "data" : dataex }

            consultas.append(consulta)

            proxid += 1

        except ValueError:
            print("Por favor insira valores válidos.")

opcao = int(input("Digite uma opção: "))

if opcao == 2:
     agendar()

print(*consultas)
    

       
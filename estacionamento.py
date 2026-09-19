quantidade = 0
valores = []
valort = 0
m3 = 0

placa = input("Informe a placa do veículo: ")

while placa.upper() != "FIM":
    try:
    
        horas = float(input("Quantas horas o veículo ficou estacionado? "))
        
        while horas <= 0:
            horas = float(input("Informe quantas horas o veículo ficou( O horário fornecido deve ser maior do que 0.)"))

    
        if horas > 0 and horas < 1:
            valort = valort + 10
            valores.append(10)
            quantidade = quantidade + 1
        
        elif horas >= 1 and horas <= 3:
            valort = valort + 18
            valores.append(18)
            quantidade = quantidade + 1
        
        elif horas > 3:
            valort = valort + 30
            valores.append(30)
            m3 = m3 + 1
            quantidade = quantidade + 1
            
        placa = input("Digite a placa do próximo veículo: ")
    
    except ValueError:
        print("Insira valores válidos.")
        
if quantidade == 0:
    print("Nenhum Veículo foi registrado.")
    
else:
        
    mvalor = max(valores)
    menvalor = min(valores)
        
    print(f"O valor total arrecadado foi de: {valort}.")
    print(f"O número de veículos que ficaram mais de 3 horas foi de: {m3}.")
    print(f"O maior valor arrecadado foi de: {mvalor}.") 
    print(f"O menor valor arrecadado foi de: {menvalor}.")  
    print(f"O número de veículos registrados foi de: {quantidade}.")
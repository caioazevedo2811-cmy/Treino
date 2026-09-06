notas = []
total = 0

while len(notas) < 5:
    try:

        nota = float(input("Informe a nota do aluno: "))

        total = total + nota

        notas.append(nota)

    except ValueError:
        print("Informe apenas números.")

media = total/len(notas)
maior = max(notas)
menor = min(notas)

print("As notas foram:" , *notas) 
print(f"A maior nota foi: {maior}.")
print(f"A menor nota foi: {menor}. ")
print(f"A media das notas foi de: {media}.")









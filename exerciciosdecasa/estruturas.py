notas = []
qnt = int(input("Quantas notas?"))

for i in range(qnt):
    nota= float(input(f'Nota {i+1}:'))
    notas.append(nota)

media = sum(notas)/len(notas)
print(media)
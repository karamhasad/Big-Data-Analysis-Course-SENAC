numero =''
soma = 0
while numero != 0:
    numero =int(input('Digite um numero'))
    if numero >0:
        soma+=+numero
else:
    print(f'Voce escolheu parar o ciclo e a soma ficou em {soma}')
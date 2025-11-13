def somar(a, b):
    return a + b

def subt(a,b):
    return a - b

def divi(a,b):
    if b!= 0:
        return a/b
    else:
        print('Valor invalido')

def mult(a,b):
    return a*b

num1= int(input("Digite o primeiro número"))
num2= int(input("Digite o primeiro número"))
escolha = input("Digite uma opção 1 - somar, 2 subtrair, 3 - multiplicar, 4 - dividir")

if escolha == '1':
    x=somar(num1,num2)
elif escolha == '2':
    x=subt(num1,num2)
elif escolha == '3':
    x=mult(num1,num2)
elif escolha == '4':
    x=divi(num1,num2)
else:
    print(f'Voce escolheu uma entrada invalida ({escolha}). Tente novamente')
# x=divi(num1, num2)
print(f"Resultado da operação: {x}")


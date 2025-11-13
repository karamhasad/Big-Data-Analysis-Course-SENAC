def indicador(a,b):
    if a > b: 
        return (f"{a} é maior que {b}")
    else:
        return (f"{b} é maior que {a}")

num1= int(input('Digite um numero'))
num2= int(input('Digite outro numero'))

maior=indicador(num1,num2)
print(maior)
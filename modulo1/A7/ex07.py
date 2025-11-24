def ehpar(num):
    return num % 2 == 0

num =int(input('digite um numero'))
resultado=ehpar(num)
if resultado:
    print 
else:
    print(f"O numero {num} é impar")


def quadrado(lado):
    return lado ** 2

medida_lado=float(input("Digite a medida do lado do quadrado"))

area=quadrado(medida_lado)
print(f"A area do quadrado é {area}")
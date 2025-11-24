senhasorteio= 34
tentativa=''
while tentativa != 34:
    tentativa=int(input('Digite sua tentativa:'))
    if tentativa <10:
        print('Sua tentativa passou longe para baixo')
    elif tentativa > 40:
        print('Sua tentativa esta acima!')
    elif tentativa < 40 and tentativa >35:
        print('Está quente!')

else:
    print(f'Voce acertou a senha, que era {senhasorteio}. Parabens!')
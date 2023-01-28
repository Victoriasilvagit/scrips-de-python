# praticando a programar tudo em inglês
km = float(input('How many kilometers is the trip?'))

if km <= 200:
    p1 = km * 0.50
    print('The price of your ticket will be R${:.2f}'.format(p1))
else:
    p2 = km * 0.45
    print('The price of your ticket will be R${:.2f}'.format(p2))

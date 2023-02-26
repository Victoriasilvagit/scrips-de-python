peso = float(input('Peso:'))
altura = float(input('Altura:'))
imc = peso / (altura ** 2)

print('Seu imc é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif  imc < 25:
    print('Peso ideal')
elif  imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade morbida')
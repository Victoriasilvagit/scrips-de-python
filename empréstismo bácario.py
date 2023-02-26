casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
fina = int(input('Quantos anos de financiamento?'))
pretacao = casa / (fina * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa no valor de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, fina, pretacao))
if pretacao <= minimo:
    print('Parabéns empréstimo concedido!')
else:
    print('Empréstimo negado, pois prestação mensal excede 30% do salário')
    
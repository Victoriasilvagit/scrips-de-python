sal = float(input('Informe o seu salario para calcular o reajuste:'))
if sal <= 1250:
    novo = sal + (sal * 15/100)
    print('O novo salário é de R${:.2f} com o novo reajuste'.format(novo))
else:
    novo = sal + (sal * 10/100)
    print('O novo salário é de R${:.2f} com o novo reajuste'.format(novo))
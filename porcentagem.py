#ex01
p = float(input('Informe o preço do produto:'))
d = p * 5/100
print('O preço do produto com o desconto de 5% é {}'.format(p-d))
#ex02
salario = float(input('Informe seu salário: R$'))
desc = salario * 15 / 100
print('O salario com o reajuste  de 15%  corresponde a R${:.0f}'.format(desc+salario))

n1 = 5
n2 = 3
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# \n quebra linhas
#o end do final serve para os prints não quebrarem linha
print('A soma é {}, o produto é {} e a divisão  é {:.3f}'.format(s, m, d), end=' ')
print('Divisão  inteira {} e potência {}'.format(di, e))
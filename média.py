#exemplo 01
n = float(input('Digite um numero:'))
print('O dobro de {} vale {}.	\n O triplo de {} vale {}.\n A raiz quadrada de {} é igual a {:.2f}'.format(n, (n*2), n, (n*3), n, pow(n, (1/2))))
#exemplo 02
n1 = float(input('Primeira nota do aluno:'))
n2 = float(input('Segunda nota do aluno:'))
print('A media entre {} e {} é {:.2f}'.format(n1, n2, (n1+n2)/2))
#exemplo 03
med = float(input ('Distância em metros:'))
cm = med * 100
mm = med * 1000
print('A medida de {}m corresponde a {}cm e {}mm'.format(med, cm, mm))

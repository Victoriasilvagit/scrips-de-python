num = int(input('Digite um número inteiro:'))
op = int(input('Escolha uma das bases para conversão:\n [1] Converter para binário\n [2] Converter para octal\n [3] Converter para hexadecimal\n Sua opção:'))

if op == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)[2:]))
elif op == 2:
     print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif op == 3:
     print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida')
    

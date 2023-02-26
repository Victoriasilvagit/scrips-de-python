from datetime import date
ano_atual = date.today().year
sexo = int(input('Você é Homem? Se sim, digite 1. Senão, digite 2:'))
if sexo == 2:
      print('Você não precisa se aliastar!')
elif sexo == 1:
    nasc = int(input('Ano de nascimento:'))
    idade = ano_atual - nasc
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, ano_atual))
    if idade == 18:
        print('Você tem que se alistar Imediamente!')
    elif idade < 18:
        saldo = 18 - idade
        print ('Ainda faltam {} anos para o alimento'.format(saldo))
        ano =ano_atual + saldo
        print('Seu alistamento será em {}.'.format(ano))
    else:
        saldo = idade - 18
        print ('Você já deveria ter se alistado há {} anos.'.format(saldo))
        ano = ano_atual - saldo
        print('Seu alistamento foi em {}'.format(ano))
else:
    print('Número informado invalido!')
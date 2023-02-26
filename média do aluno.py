n1 = float(input('Informe a primeria nota:'))
n2 = float(input('Informe a segunda nota:'))

media = (n1+n2)/2
if media < 5.0:
    print('A média do aluno é {:.1f}, ele está reprovado!'.format(media))
elif 6.9 > media >= 5.0:
     print('A média do aluno é {:.1f}, ele está de recuperação!'.format(media))
else:
     print('A média do aluno é {:.1f}, ele está aprovado!'.format(media))

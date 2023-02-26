from datetime import date
nasc = int(input('Em que ano você nasceu?'))
atual = date.today().year
idade = atual - nasc

if idade <= 9:
    print('A categoria desse ateta é Mirim, pois sua idade é {} anos'.format(idade))
elif idade <= 14:
    print('A categoria desse ateta é Infatil, pois sua idade é {} anos'.format(idade))
elif idade <= 19:
    print('A categoria desse ateta é Júnior, pois sua idade é {} anos'.format(idade))
elif idade <= 25:
    print('A categoria desse ateta é Sênior, pois sua idade é {} anos'.format(idade))
else:
    print('A categoria desse ateta é Master, pois sua idade é {} anos'.format(idade))

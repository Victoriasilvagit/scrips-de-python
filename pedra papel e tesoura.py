from random import randint
from time import sleep
itens = ('Pedra', 'Papel','Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Você ganhou!')
    elif jogador == 2:
        print('Computador ganhou!')
    else: 
        print('Jogada inválida!')
elif computador == 1:
    if jogador == 0:
        print('Computador ganhou!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Você ganhou!')
    else: 
        print('Jogada inválida!')
elif computador == 2:
    if jogador == 0:
        print('Você ganhou!')
    elif jogador == 1:
        print('Computador ganhou')
    elif jogador == 2:
        print('Empate')
    else: 
        print('Jogada inválida!')
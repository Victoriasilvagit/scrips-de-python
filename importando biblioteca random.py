#ex01
#choice escolhe um dos itens 
from random import choice 
n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')
li = [n1, n2, n3, n4] 
print ('O aluno escolhido foi {}'.format(choice(li)))

#ex02
#shuffle embaralha 
from random import shuffle
n1 = input('Primeiro Aluno:')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno:')
li = [n1,n2, n3, n4]
shuffle(li) 
print('A ordem de apresentação  dos alunos será:')
print(li)
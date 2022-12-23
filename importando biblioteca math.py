#ex01
import math 
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raiz de {} é {}'.format(num, math.ceil(raiz)))

#ex02
from math import trunc 
num = float(input('Digite um número:'))
print('O número {} tem a parte inteira {}'.format(num, trunc(num)))

#ex03
from math import hypot
co = float(input('qual o valor do cateto oposto:'))
ca = float(input('qual o valor do cateto adjacente:'))
hi = hypot(ca, co)
print('A hipotenusa vai medir {:.2f}'.format(hi))

#ex04
import math
ang = float(input('Digite o ângulo que você deseja:'))
sen = math.sin(math.radians(ang))
co = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('o Ângulo de {}° tem o seno de {:.2f}, o cosseno {:.2f} e a tangente de {:.2f}'.format(ang, sen, co, tang))
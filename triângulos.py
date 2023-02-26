print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
r1 = float(input('Primeiro segmento?'))
r2 = float(input('Segundo segmento?'))
r3 = float(input('Terceiro segmento?'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r3:
    if r1 == r2 and r2 == r3:
        print('O triângulo formado é um équilátero, pois seus lados são todos iguais.')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('O triângulo formado é um escaleno, pois todos os lados são diferentes')
    else:
        print('O triângulo formado é um Isóceles, pois dois lados são iguais.')
else:
    print('Os segmentos acima não formam um triângulo!')
    
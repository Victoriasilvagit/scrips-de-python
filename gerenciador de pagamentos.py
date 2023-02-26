compra = float(input('Preço das compras:'))
print('''Formas de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3X  ou mais no cartão ''')
opc = int(input('Qual a forma de pagamento?'))

if opc == 1:
    desc = (compra*10)/100
    novo = compra - desc
    print('As compras no dinheiro ou cheque tem um desconto de 10%. Sua compra de R${:.2f} vai custar R${:.2f}'.format(compra, novo))
elif opc == 2:
    desc = (compra*5)/100
    novo = compra - desc
    print('As compras á vista no cartão tem um desconto de 5%. Sua compra de R${:.2f} vai custar R${:.2f}'.format(compra, novo))
elif opc == 3:
    novo = compra / 2
    print('As compras parceladas em 2x no cartão vai custar R${:.2f}'.format(novo))
elif opc == 4:
    num = int(input('Quantas parcelas serão?'))
    desc = compra + (compra*20/100)
    novo = desc / num
    print('As compras parceladas em 3x ou mais no cartão possui um juros de 20%.Cada parcela vai custar R${:.2f} o valor total da compra é R$ {:.2f}'.format(novo, desc))
else:
    print('Opção invalida')
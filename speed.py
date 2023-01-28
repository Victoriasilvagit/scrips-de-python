# praticando a programar tudo em inglês
speed = float(input('Enter the speed at whichthe car was:'))
if speed  > 80:
    tk = (speed - 80) * 7
    print('Fined! This car has exceeded the permitted speed limit which is 80km/h. The amount to be paid is U${:.2f}'.format(tk))
else:
    print('will not be fined')
a=float(input('enter your score(0,20): '))
if 0<=a<10 :
        print('failed')
elif 10<=a<12 :
    print('poor pass')
elif 12<=a<15 :
    print('average pass')
elif 15<=a<17 :
    print('passed')
elif 17<=a<20 :
    print('excellent pass')
else :
    print('the score you have entered is out of range')

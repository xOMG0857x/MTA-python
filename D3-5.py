try:    
    a=int(input('輸入被除數'))
    if a<0:
        print('請輸入正整數')
    else:
        b=int(input('輸入除數'))
        if b<0:
            print('請輸入正整數')
        else:
            r=a/b
            print(a,'除以',b,'=',r)
except ValueError:
    print('輸入了非數字的值')
except ZeroDivisionError:
    print('除數不可為0')

import random
ans = random.randint(1,100)
times=0
while True:
    guess= int(input('猜數字'))
    times+=1
    if ans>guess:
        print('太小')
        continue
    elif ans>guess:
        print('太大')
        continue
    else:
        print('right')
        print('總共用了',times,'次')
        break

        
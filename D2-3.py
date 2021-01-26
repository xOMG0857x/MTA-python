score_list=[]
i=1
numbers=int(input('人數?'))
for i in range(numbers):
    score=int(input('score?'))
    if score<=60:
        score=60
    score_list.append(score)
    i+=1
    if i == numbers:
        print('全班成績',score_list)
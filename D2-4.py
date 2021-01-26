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
        score_list.sort()
        print('全班最高:',score_list[len(score_list)-1],'分')
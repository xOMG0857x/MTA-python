a=0
for i in range(100):
    a+=1
    if a%3!=0 and a%5!=0:
        print(a)
    else:
        continue
import time as t

play = t.clock()
for i in range(0,1000):
    for j in range(0,1000):
        n=i*j
stop= t.clock()
print(str(stop-play)) 
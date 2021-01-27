a=int(input('有多少?'))
b=int(input('取多少?'))
import random
numbers=random.sample(range(a),b)
numbers.sort()
special=numbers.pop()
print('抽到:',numbers)
print('特別號碼為:',special)
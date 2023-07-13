'''from collections import Counter
str1 = 'hello'
counting = Counter(str1)
print(counting)
print(counting.items())
print(counting.keys())
print(counting.values())
print(counting.most_common(2))
print(counting.most_common(2)[1])
print(list(counting.elements()))'''

'''
from collections import namedtuple
maths = namedtuple('Numbers','a,b')
num = maths(13,14)
print(num)
sum = 0
for i in num:
    sum+=i
print(sum)
'''
'''
from collections import OrderedDict
dict1 = {}
dict1[0] = 'a'
dict1[1] = 'b'
dict1[2] = 'ab'
print(dict1)
'''
'''
from collections import defaultdict
arr = defaultdict(int)
arr[0] = 0.223
arr[1] = 1.23
arr[2] = 344
print(arr)
'''
from collections import deque
arr = deque([1,2,3,4,5,6])
arr.appendleft(9)
print(arr)
arr.append(10)
print(arr)

if arr[-1]>13:
    arr.pop()
else:
    arr.appendleft(8)
print(arr)
if len(arr)>10:
    print('enough number in the list')
else:
    arr.extend([11,12,13])
print(arr)
arr.rotate(1)
print(arr)
arr.rotate(1)
print(arr)

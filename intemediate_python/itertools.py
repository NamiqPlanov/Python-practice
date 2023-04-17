'''from itertools import product
a = [1,3]
b= [2,4]
prod = list(product(a,b,repeat=2))
print(sorted(prod))
'''

from itertools import permutations

arr = [1,3,5,7]
perm = list(permutations(arr,4))
print(perm)

from itertools import combinations,combinations_with_replacement
arr = [10,20,15,9]
arr2 = sorted(arr)
comb = list(combinations(arr2, 3))
print(comb)
comb_replace = list(combinations_with_replacement(arr2, 3))
print(comb_replace)


from itertools import accumulate
import operator
arr = [12,13,11,14]
acc1 = list(accumulate(arr,func=operator.mul))
acc2 = list(accumulate(arr,func=operator.add))
print(acc1)
print(acc2)
acc3 = list(accumulate(arr,func=max))
print(acc3)
acc4 = list(accumulate(arr,func=min))
print(acc4)



from itertools import groupby

def even(i):
    return i%2==0
arr = [10,11,12,14]
evengroup = groupby(arr,key=lambda i:i%2==0)
for a,b in evengroup:
    print(a,list(b))





info = [
    {'name':'Namiq','age':19},
    {'name':'Surxay','age':35},
    {'name':'John','age':24}
    ]

infogroup = groupby(info,key=lambda a:a['age']>=23)
for key,value in infogroup:
    print(key,list(value))


from itertools import count,cycle,repeat


try:
    number = int(input('enter number for starting count function:'))
    if number>30:
        print('numbers that are more than 30 are not allowed to enter')
    else:
        for a in count(number):
            print(a)
            if a==30:
                break
except:
    print('no')


arr = [1,2,3,4]
for x in repeat(arr,4):
    print(x)
    





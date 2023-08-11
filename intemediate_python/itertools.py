'''
from itertools import product
a = [1,2,3]
b = [4,5,6]
prod = list(product(a,b,repeat=3))
print(prod)
'''
'''
from itertools import permutations
a = [1,2,4,5]
perm = permutations(a)
print(list(perm))
    '''

'''from itertools import combinations,combinations_with_replacement
a = [1,2,3]
comb = combinations(a,2)
print(list(comb))

comb_rep = combinations_with_replacement(a,3)
print(list(comb_rep))
'''
'''
from itertools import accumulate
import operator
a = [10,20,30,40,50]
accum = accumulate(a,func=operator.add)
print(list(accum))
'''

from itertools import groupby
a = ['hello','bro','good']
def longer_than_three(i):
    return len(i)>=4
    
group = groupby(a,key=longer_than_three)
for key,value in group:
    print(key,list(value))



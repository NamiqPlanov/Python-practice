'''set1 = {1,3,4,5,2,3}
print(set1)
set2 = set(set1)
print(set2)
print(type(set1))
set1.add(6)
print(set1)
set2.update(set1)
print(set2)
set2.remove(3)
print(set2)
set2.discard(4)
print(set2)

for i in set2:
    if i%2==0:
        print(i)
'''
set1 = {10,20,30,40,50}
set2 = {10,40,20}
'''
u = sorted(set1.union(set2))

print(u)
i = set1.intersection(set2)
print(i)
for i in set1:
    for j in set2:
        if i==j:
            print('yes')
            break
    
dif = set1.difference(set2)
print(dif)
sym_def = set1.symmetric_difference(set2)
print(sym_def)
'''
set2.intersection_update(set1)
print(sorted(set2))
set1.difference_update(set2)
print(set1)
set2.symmetric_difference_update(set1)
print(set2)
print(set2.issubset(set1))
print(set1.issubset(set2))
print(set2.issuperset(set1))
print(set2.isdisjoint(set1))


set3 = {'a','b','c','d',345}
set4 = {'w','e','r',234,54}
set5 = set4.copy()
print(set5)
set5.add('y')
print(set5)
set5 = set3
print(set5)
set5 = frozenset(set4)
print(set5)

           




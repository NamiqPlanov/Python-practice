''' 
set1 = {1,2,3,4,1,2,3}
print(set1)
set2 = set('Namiq')
print(set2)
set3 = set()
set3.add('n')
set3.add('a')
set3.add('m')
set3.add('i')
set3.add('q')
set3.discard('a')
print(set3)
set3.pop()
print(set3)
'''
'''
myset = set('Namiq')
for a in myset:
    print(a)
'''
set1 = {1,2,3,4,5}
set2 = {-1,-2,-3,-4,-5,9,8}
set3 = {6,7,8,9,10}
union = set1.union(set2)
overall = union.union(set3)
sorted_set = sorted(overall)
print(sorted_set)


try:
    intersect = set1.intersection(set2)
    print(intersect)
except:
    print('error')

difference = set1.difference(set2)
print(difference)
symmetricdif = set1.symmetric_difference(set2)
print(symmetricdif)
set2.update(set3)
print(set2)
set2.intersection_update(set3)
print(set2)
print(set1.issubset(set2))
print(set2.issuperset(set3))




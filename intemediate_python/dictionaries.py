dict1 = {'name':'Namiq','lastname':'Planov'}
'''
print(dict1)
name = dict1['name']
print(name)
add = dict(name='Ayxan',lastname='Planov')
print(add)
dict1['year'] = 2003
print(dict1)
del dict1['name']
print(dict1)
dict1.pop('lastname')
print(dict1)
dict1.popitem()
print(dict1)
try:
    print(len(dict1))
except:
    print('no')

for key,values in dict1.items():
    print(key,'-',values)
'''

dict2 = dict(name='Ayxan',lastname='Planov')
print(dict1)
print(dict2)
dict2.update(dict1)
print(dict2)

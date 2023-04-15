dict1={
    'name':'Namiq',
    'last_name':'Planov',
    'age':19,
    'city':'Baku'
}
'''print(dict1)
dict2 = dict(name='Namiq',age=19,city='Baku')
print(dict2)


val1 = dict1['name']
val2 = dict1['last_name']
print(val1)
print(val2)
dict1['region']='Nesimi'
print(dict1)
del dict1['last_name']
print(dict1)
dict1.pop('name')
print(dict1)
dict1.popitem()
print(dict1)



if 'name' in dict1:
    print(dict1['name'])
else:
    raise Exception('no')

try:
    print(dict1['region'])
except:
    print('noo')


for key in dict1.keys():
    print(key)
for val in dict1.values():
    print(val)

for key,val in dict1.items():
    print(key,'-',val)

dict2 = dict1.copy()
dict2['name'] = 'Ayxan'
print(dict2)
print(dict1)
'''
dict2 = dict(name='Ayxan',age=15,city='Shamakhi')
dict1.update(dict2)
print(dict1)

    
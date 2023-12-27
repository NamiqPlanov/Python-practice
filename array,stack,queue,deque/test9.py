list1 = []
n = int(input('number of nodes:'))
for i in range(n):
    list1.append(int(input('enter node:')))
print('Data={}'.format(list1))
len1 = len(list1)
list1.remove(list1[len1//2])
for j in range(len(list1)):
    print('Data={}'.format(list1[j]))
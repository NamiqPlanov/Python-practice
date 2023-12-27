list1 = []
n = int(input('number of nodes:'))
for i in range(n):
    list1.append(int(input('enter node:')))
for j in range(len(list1)):
    print('Data={}'.format(list1[j]))

a = int(input('Input the element to be searched:'))
if a in list1:
    print('element found at node:{}'.format(list1.index(a)))
else:
    print('not valid element')
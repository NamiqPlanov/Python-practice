list1 = []
n = int(input('how many nodes:'))
for i in range(n):
    list1.append(int(input('Enter node:')))
print('list={}'.format(list1))
list1.append(int(input('Ente the number:')))
for j in range(len(list1)):
    print('Data = {}'.format(list1[j]))


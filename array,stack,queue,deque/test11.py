from queue import Queue

queue1 = Queue()
n = int(input('How many nodes:'))
for i in range(n):
    queue1.put(int(input('add node:')))
sum1 = 0
count=0
while not queue1.empty():
    elem = queue1.get()
    if elem%2!=0:
        print(elem)
        sum1+=elem
        count+=1
avg1 = sum1/count
print(avg1)


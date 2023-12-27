from queue import Queue

queue1 = Queue()
n = int(input('How many nodes:'))
for i in range(n):
    queue1.put(int(input('add node:')))
reversed_elem = []
while not queue1.empty():
    reversed_elem.insert(0,queue1.get())

print(reversed_elem)
sum_reversed = sum(reversed_elem)
print(sum_reversed)
from queue import Queue

queue1 = Queue()
n = int(input('How many nodes:'))
for i in range(n):
    queue1.put(int(input('add node:')))
sorted_elem = sorted(queue1.queue)
second_lowest = sorted_elem[1]
while not queue1.empty():
    current_element =queue1.get()
    if current_element == second_lowest:
        print(f"Removed element {second_lowest} from the queue.")
    else:
        queue1.put(current_element)

print(queue1.queue)
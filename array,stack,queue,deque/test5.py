stack = []
stack.append(0)
stack.append(1)
stack.append(5)
stack.append(2)
stack.append(4)
stack.append(7)
print(stack)
reverse_stack = stack[::-1]
print(reverse_stack)
reverse_stack.pop()
reverse_stack.pop()
print(reverse_stack)
reverse_stack.insert(0,-1)
reverse_stack.insert(0,10)
print(reverse_stack)
turn_arr = reverse_stack[::-1]
print(turn_arr)


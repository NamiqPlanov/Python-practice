stack = []
stack.append(5)
stack.append(2)
stack.append(2)
stack.append(4)
stack.append(7)
print(stack)
filtered_list = [x for x in stack if x!=2]
print(filtered_list)
filtered_list.insert(2,5)
filtered_list.insert(1,7)
filtered_list2 = [a for a in filtered_list if a!=7]
print(filtered_list2)
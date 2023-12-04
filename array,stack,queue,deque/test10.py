stack=[]
stack.append(5)
stack.append(2)
stack.append(4)
stack.append(7)
len1 = len(stack)
print(stack)

middle1 = stack[len1//2]
stack.remove(middle1)
print(stack)
stack.insert(0,-1)
stack.insert(0,-2)
len2 = len(stack)
middle2 = stack[len2//2]
stack.remove(middle2)
print(stack)
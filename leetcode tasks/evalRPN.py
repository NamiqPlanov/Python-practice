def function(token):
    stack = []
    for i in token:
        
        if i=='+':
            stack.append(stack.pop()+stack.pop())
        elif i=='*':
            stack.append(stack.pop()*stack.pop())
        elif i=='-':
            a = stack.pop()
            b=stack.pop()
            stack.append(int(b-a))
        elif i=='/':
            a = stack.pop()
            b=stack.pop()
            stack.append(int(b/a))
        else:
            stack.append(int(i))
    return stack[0]

print(function(["2","1","+","3","*"]))

def isvalid(str):
    stack = []
    clostoopen = {')':'(',']':'[','{':'}'}
    for i in str:
        if i in clostoopen:
            if stack and stack[-1]==clostoopen[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)

    return True if not stack else False

print(isvalid('[)'))



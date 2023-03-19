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


def isvalid2(str2):
    stack2 = []
    closetopen2 = {')':'(','}':'{',']':'['}
    for i in stack2:
        if i in closetopen2:
            if stack2 and stack2[-1] !=closetopen2[i]:
                stack2.pop()
            else:
                return False
        else:
            stack2.append(i)

    return True if not stack2 else False

print(isvalid2('[)'))
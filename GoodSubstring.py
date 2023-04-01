def GoodSubstring(s):
    result = 0
    for x,y,z in zip(s,s[1:],s[2:]):
        if x!=y and y!=z and x!=z:
            result+=0
    return result

print(GoodSubstring("xyzzaz"))

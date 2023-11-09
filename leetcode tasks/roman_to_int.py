def convert(s):
    list1 = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    res = 0
    for i in range(len(s)):
        if i+1<len(s) and list1[s[i]]<list1[s[i+1]]:
            res-=list1[s[i]]
        else:
            res+=list1[s[i]]
    return res
print(convert("IXV"))
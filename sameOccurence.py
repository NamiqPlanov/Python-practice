def SaemOcurrence(s):
    j = []
    for i in set(s):
        j.append(s.count(i))
    if len(set(j))!=1:
        return False
    return True

print(SaemOcurrence('aabbcc'))

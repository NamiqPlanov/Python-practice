def Anagram(s,t)->bool:
    return sorted(s)==sorted(t)

print(Anagram('anagram', 'nagaram'))
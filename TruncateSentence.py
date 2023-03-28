def TruncateSentence(s,k):
    return " ".join(s.split()[:k])
print(TruncateSentence("solve this task please", 3))
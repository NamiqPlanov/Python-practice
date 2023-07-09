def ManyWords(sentences):
    return max(s.count(' ') for s in sentence)+1
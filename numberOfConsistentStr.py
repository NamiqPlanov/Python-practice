def ConsStr(allowed,words):
    not_match = 0
    for word in words:
        for k in word:
            if k not in allowed:
                not_match+=1
                break
    answer = len(words)-not_match
    return answer

print(ConsStr('hello', ['el','lo','ec','ac','ll']))
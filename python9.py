def Countwords(word1,word2):
    sameword = list(set(word1) and set(word2))
    answer = 0
    for i in sameword:
        if word1.count(i) ==1 and word2.count(i)==1:
            answer+=1
    return answer
print(Countwords(['Boy','Friend','Hello'], ['Goodbye','Hello','Boy']))




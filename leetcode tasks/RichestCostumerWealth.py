def RichestCostumer(accounts):
    answer = 0
    current = 0
    for i in accounts:
        for j in i:
            current+=j
        answer = max(answer,current)
        current = 0
    return answer

print(RichestCostumer([[1,10,6],[2,15,4]]))



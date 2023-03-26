def MostCandies(candies,extracandies):
    answer = []
    maximum = max(candies) 
    n = len(candies)
    for i in range(n):
        if candies[i]+extracandies >=maximum:
            answer.append(True)
        else:
            answer.append(False)
    return answer

print(MostCandies([1,2,3,4,5,6], 2))

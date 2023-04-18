def maxpos(arr):
    negative = 0
    positive = 0
    for i in arr:
      if i>=0:
         break
      else:
        negative+=1

    for i in reversed(arr):
        if i<=0:
            break
        else:
            positive+=1
    return max(positive,negative)
print(maxpos([-2,-1,0,1,2,3,4]))

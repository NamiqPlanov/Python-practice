def canJump(arr):
    goal = len(arr)-1
    for i in range(len(arr)-1,-1,-1):
        if i +arr[i]>=goal:
            goal = i
    return True if goal ==0 else False

print(canJump([1,-2,3,4,7]))
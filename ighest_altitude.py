def highest_altitude(gain):
    result = [0]
    n = len(gain)
    for i in range(n):
        temp = result[i]+gain[i]
        result.append(temp)
    return max(result)
print(highest_altitude([-3,5,2,4,9]))
def RingRods(rings):
    rods = [set() for _ in range(10)]
    answer = 0
    n = len(rings)
    for i in range(0,n,2):
        rods[int(rings[i+1])].add(rings[i])
    for j in rods:
        if len(j)>=3:
            answer+=1
    return answer
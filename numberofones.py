def maxnumberofones(mat):
    mx = 0
    for row in mat:
        mx = max(mx,sum(row))
    for i,row in enumerate(mat):
        if mx ==sum(row):
            return [i,sum(row)]
    return []
print(maxnumberofones([[0,0,0],[0,1,1]]))

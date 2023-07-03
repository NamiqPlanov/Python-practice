def oddcells(m,n,indices):
    row_data = [0]*m
    col_data = [0]*n
    for tup in indices:
        row_data[tup[0]] = row_data[tup[0]]+1
        col_data[tup[1]] = col_data[tup[1]]+1
    odd_count = 0
    for i in range(m):
        for j in range(n):
            val = row_data[i]+col_data[j]
            if val%2!=0:
                odd_count+=1
    return odd_count
print(oddcells(2,2,[[0,1],[1,1]]))
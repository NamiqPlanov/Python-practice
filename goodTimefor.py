def stock(prices):
    l = 0
    r = 1
    maxPrice = 0
    while r<len(prices):
        if prices[l]<prices[r]:
            profit = prices[r]-prices[l]
            maxPrice = max(maxPrice, profit)
        else:
            l=r
        r+=1
    return maxPrice

print(stock([1,2,3,4,5,6,8]))
def goodpairs(arr):
    n = len(arr)
    result = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                result+=1
        return result


print(goodpairs([1,2,1,3,4,5,3]))


 repeat = {}
        num = 0
        
        # for every element in nums
        for v in nums:
            
            # number of repeated digits
            if v in repeat:
                
                # count number of pairs based on duplicate values
                if repeat[v] == 1:
                    num += 1
                else:
                    num += repeat[v]
                
                # increment the number of counts
                repeat[v] += 1
            # number has not been seen before
            else:
                repeat[v] = 1
        # return
        return num
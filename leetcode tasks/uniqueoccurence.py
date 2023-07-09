def uniqueoccurence(arr):
    hashmap = {}
    for i in hashmap:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i]=1
    list_hashmap = list(hashmap.values())
    count_hashmap = {}
    for i in list_hashmap:
        if i in count_hashmap:
            return False
        count_hashmap[i]=1
    return True
print(uniqueoccurence([1,1,2,3,3,3]))
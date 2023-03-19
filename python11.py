

def elementexists(arr,target):
    for i in arr:
        if target ==i:
            return True
    return False
print(elementexists([1,2,3,4],2))
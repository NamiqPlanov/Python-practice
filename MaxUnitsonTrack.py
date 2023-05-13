def maxunits(boxsize,trucksize):
    boxsize.sort(key=lambda a:-a[1])
    capacity=0
    for box,unit in boxsize:
        if capacity>=box:
            trucksize-=box
            capacity+=box*unit
        else:
            capacity+=trucksize*unit
            break
    return capacity
print(maxunits([[2,4],[3,1]], 2))
def Destination(paths)->str:
    A,B = map(set(zip(*paths)))
    return (B-A).pop()

print(Destination([['Baki','Samaxi'],['Quba','Qusar'],['Yevlax','Gence']]))
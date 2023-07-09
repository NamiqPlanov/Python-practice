
n = int(input('enter number of rows:'))
l = int(input('enter number of columns:'))

for i in range(n+2):
    for j in range(l):
        if i==0 or j == l-1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    



        

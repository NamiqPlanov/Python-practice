#n = int(input('enter number of rows: '))
#for i in range(n):
#    for j in range(n-i-1):
 #       print(" ",end = "")
 #   for j in range(i+1):
 #       print("*",end=" ")
 #   print()



#l = int(input('enter number of rows: '))
#for i in range(l):
 #   for j in range(i):
  #      print(" ",end="")
   # for j in range(l-i):
    #    print("*",end=" ")
    #print()


#row = int(input('enter number of rows: '))
#column = int(input('enter number of columns: '))
#for i in range(row):
 #   for j in range(column):
  #      if i==0 or i ==(row-1) or j==0 or j == (column-1):
   #         print("*",end=" ")
    #    else:
     #       print(" ",end=" ")
    #print()



a = int(input('enter number of rows: '))
for i in range(a):
    for j in range(i+1):
        print("*",end=" ")
    print()


b = int(input('number of rows: '))
for i in range(b):
    for j in range(b-i):
        print("*",end=" ")
    print()

c = int(input('enter number of rows: '))
d = int(input('enter number of columns: '))
for i in range(c):
    for j in range(d):
        print("*",end=" ")
    print()

import sys

prices = [10,20,30,40,50]
halved = []
for price in prices:
    half_price = price/2
    halved.append(half_price)

print(halved)

halved2 = [price/2 for price in prices]
print(halved2)



flights = ['737','456','545']
arr = []
for flight in flights:
    full_flight_name = 'aero'+flight
    arr.append(full_flight_name)
print(arr)

compehension = ['aero'+flight for flight in flights]
print(compehension)
print(sys.getsizeof(compehension))
print(sys.getsizeof(arr))




answers = [True,True,False,True]
opposite = [not answer for answer in answers]
print(opposite)


words = ['hello','hallo','allo']
letters = [word.count('l') for word in words]
print(letters)



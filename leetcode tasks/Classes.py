class CarInfo:
    def __init__(self,name,year,owner,old_new):
        self.name = name
        self.year = year
        self.owner = owner
        self.old_new = old_new
    def sentence(self):
        return 'The car is {}. Its year of release is {}.Its owner is {}.This car is {}'.format(self.name,self.year,self.owner,self.old_new)
        

car1 = CarInfo(input('enter name:'), int(input('enter year:')), input('enter owner:'), input('is this car new or old?'), )
print(car1.name)
print(car1.sentence())

car1.sentence()
print(CarInfo.sentence(car1))







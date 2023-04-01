

class Student:

    def __init__(self,first_name,last_name,father_name)->None:
        self.first_name = first_name
        self.last_name = last_name
        self.father_name = father_name
    def getFullName(self):
        return '{} {} {}'.format(self.first_name,self.last_name,self.father_name)

    def __str__(self)->str:
        return self.getFullName()






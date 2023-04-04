class Person:
    def __init__(self,first_name=None,last_name=None,father_name=None):
        self.first_name = first_name
        self.last_name = last_name
        self.father_name = father_name
    
    def GetfullName(self):
        return '{} {} {}'.format(self.first_name,self.last_name,self.father_name)

    def __str__(self)->str:
        return self.GetfullName()


class Student(Person):
    def __init__(self,first_name=None,last_name=None,father_name=None)->None:
        super().__init__(first_name,last_name,father_name)

        self.__is_starosta = False

    def makestarosta(self):
        self.__is_starosta = True

    def isstarosta(self):
        return self.__is_starosta


class Teacher(Person):
    def __init__(self,first_name=None,last_name=None,father_name=None,subject=None)->None:
        super().__init__(first_name,last_name,father_name)
        self.subject = subject
        





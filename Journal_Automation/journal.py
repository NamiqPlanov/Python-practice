class Subject:
    def __init__(self,name:str,code:str)->None:
        self.name = name
        self.code = code

    def __str__(self)->str:
        return '{}-{}'.format(self.name,self.code)

class Person:
    def __init__(self,first_name=None,last_name=None,father_name=None):
        self.first_name = first_name
        self.last_name = last_name
        self.father_name = father_name
    def getFullName(self):
        return '{} {} {}'.format(self.first_name,self.last_name,self.father_name)

    def __str__(self)->str:
        return self.getFullName()


class Student(Person):
    def __init__(self,first_name=None,last_name=None,father_name=None,subject:Subject=None)->None:
        super().__init__(first_name,last_name,father_name)
        self.__isStarosta = False
    def makeStarosta(self):
        self.__isStarosta = True
    def isStarost(self):
        return self.__isStarosta


class Teacher(Person):
    def __init__(self,first_name=None,last_name=None,father_name=None,subject:Subject=None)->None:
        super().__init__(first_name,last_name,father_name)
        self.subject = subject

    def __str__(self)->str:
        return super().__str__() + ', subject: '+ self.subject.name

class Group:
    def __init__(self,name:str,starosta:Student):
        self.name = name

        if not starosta.isStarost():
            raise Exception('this student is not starosta')

        self.starosta = starosta
        self.students = []
        self.__subjects = []

    def addStudent(self,student:Student):
        self.students.append(student)

    def printStudentList(self):
        print('Student list: ',[str(student) for student in self.students])

    def addSubject(self,subject:Subject):
        self.__subjects.append(subject)
    def printSubject(self):
        print('Subjects: ',[str(s) for s in self.__subjects])

    def __str__(self)->str:
        return 'Group- {},starosta-{}'.format(self.name,self.starosta)


class JournalRecord:
    def __init__(self,date:str,subject:Subject,type1:str,hour:int,student:Student,is_presence:bool,mark:int=None,  )->None:
        self.date = date
        self.subject = subject
        self.type1 = type1
        self.hour = hour
        self.student = student
        self.mark = mark
        self.is_presence = is_presence

class Journal:
    def __init__(self,semestr:int,group:Group, kafedra:str):
        self.semestr = semestr
        self.group = group
        self.kafedra = kafedra

    
from student import *
class Group:
    def __init__(self,name,starosta: Student):
        self.name = name
        self.starosta = starosta

    def __str__(self)->str:
        return 'Group- {},starosta-{}'.format(self.name,self.starosta)


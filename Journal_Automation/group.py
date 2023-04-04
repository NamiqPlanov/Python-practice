from student import *

class Group:
    def __init__(self,name:str,starosta:Student):
        self.name = name

        if not starosta.isstarosta():
            raise Exception('This student is not starosta')

        self.starosta = starosta

    def __str__(self)->str:
        return 'Group-{}, starosta-{}'.format(self.name,self.starosta)
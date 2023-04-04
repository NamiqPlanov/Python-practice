class Subject:
    def __init__(self,name:str,code:str)->None:
        self.name = name
        self.code = code
    def __str__(self)->str:
        return '{} - {}'.format(self.name,self.code)
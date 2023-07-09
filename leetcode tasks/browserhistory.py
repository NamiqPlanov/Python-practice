class BrowserHostory(object):
    def __init__(self,hompage):
        """
        :type homepage:str
        """
        self.stack = [homepage]
        self.index = 0
    def visit(self,url):
        """
         :type url = str
         :rtype=None
        """
        for _in range(len(self.stack)-self.index-1):
            self.stack.pop()
        self.stack.append(url)
        self.index+=1

    def back(self,steps):
        """
        :type steps:int
        :rtype:str
        """
        if self.stack:
            self.index = max(0,self.index-steps)
            return self.stack[self.index]

    def forward(Self,steps):
        """
         :type steps:int
         :rtype:str
        """
        if self.stack:
            self.index = min(len(self.stack)-1,self.index+steps)
            return self.stack[self.index]
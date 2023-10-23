class A:
    m = 222
    def bc(self,a):
        self.m+=a

d = A()
d.bc(200)
print(d.m)



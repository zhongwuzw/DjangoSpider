class B():
    a = 2
    def __init__(self):
        pass
    
    def test(self):
        print self.a
        print self.test1()
        
class A(B):
    def __init__(self):
        self.a = 1
        
    def test1(self):
        print '3'
        
a = A()
print a.test()
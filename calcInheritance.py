class Calculation1:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def Summation(self):
        return a + b;

class Calculation2:
    def __init__(self, a, b):
        pass
    
    def Summation(self):
        return a + b;

class Calculation3(Calculation1, Calculation2):
    def __init__(self, a, b):
        Calculation1.__init__(self, a, b)
        Calculation2.__init__(self, a, b)
        
    def Division(self):
        return a/b;


#OBJECT CREATION
d = Calculation3()
print(d.Summation(10, 20))
print(d.Summation(5, 9))
print(d.Division(10, 20))

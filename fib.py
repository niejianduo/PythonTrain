class Fib(object):
    def __init__(self):
        pass
    def __call__(self,num):
        a,b = 0,1;
        self.l=[]
        
        for i in range (num):
            self.l.append(a)
            a,b= b,a+b
        return self.l
    def __str__(self):
        return str(self.l)
    __rept__=__str__
            
f = Fib()
print( f(10))

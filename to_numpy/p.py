class Geo:
    def get_pr(self,*args):
        return sum(*args)

class Square(Geo):
    def __init__(self,y):
        self.y = y

    def get_pr(self):
        return self.y * 4
    
class Rectangle(Geo):
    def __init__(self,y,x):
        self.y = y
        self.x = x

    def get_pr(self):
        return 2 * (self.y + self.x)
    
class Triangle(Geo):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    # def get_pr(self):
    #     return self.a + self.b + self.c

    
re = Rectangle(8,12)
li = Rectangle(10,10)

t1 = Triangle(4,5,3)
t2 = Triangle(9,3,22)

bi = Square(2)
gi = Square(2)

clases = [re,li,bi,gi,t1,t2]
resalt = []

for i in clases:
    li = i.get_pr()
    resalt.append(li)

print(resalt)

 
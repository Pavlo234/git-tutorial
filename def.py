class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = list (marks)
    
    def __getitem__(self,item):
        if 0 >= item >= len(self.marks):
            raise TypeError('mistek')
        return self.marks[item]

    def bym (self):
        return self.name,self.marks

    def __setitem__(self,key,value):
        if not isinstance(key,int) or key < 0:
            raise TypeError ('Индекс должно бить не отрицательным целим числом')

        if key >= len(self.marks):
            ssd = key + 1 - len(self.marks)
            self.marks.extend([0]*ssd)

        self.marks[key] = value
    
    def __delitem__(self,key):
        if not isinstance(key,int):
            raise TypeError ('Индекс должно бить не отрицательным целим числом')
        del self.marks[key]

            

s1 = Student('pavlo',[22,34,32])
pv = Student('daria',[5,6,2,12])
pv[1]= 556
print(pv.bym())

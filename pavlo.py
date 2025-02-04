#ЗАДАЧНИК
import inspect 

def binary_search(lst,search_item):#бинарный поиск йооууууу
    low = 0
    high = len(lst)-1
    search_resalt = False

    while low <= high and not  search_resalt :
        middle = (low + high)// 2
        guess = lst[middle]
        if guess == search_item:
            search_resalt = True
            return search_resalt
        if guess > search_item:
            high = middle - 1
        else:
            low = middle + 1

    return search_resalt

lst = [12,22,44,54,55,89,906]

p = 22

print(binary_search(lst,9016))




def student_runk(year):
    if year in range(1,5):
        print(f'Вы бакалавр на {year} курсе')
    elif year in range(5,6):
        print('Вы магистр')
        

def winter(month):
    if month == 1:
        print('December')
    elif month == 2:
        print('Junuary')
    elif month == 3:
        print('February')
    else:
        print('Нет такого месяца')


x = 2
if x % 5 == 0: 
    print('Х делится на 5') 
elif x % 2 == 0: 
    print('Х – четное число') 


def change(lst):
    lst[0],lst[-1] = lst[-1], lst[0]
    return lst

print(change([1,2,3,4]))

def fordtnar(name,age=100 ):
    print(name, 'is', age, 'year')

fordtnar("Максим")

r = lambda x, y : x // y
print(r(100,2))


def agrs(*args):
    print("мой любимый цвет это", args)

agrs('dhuehd')
agrs(223,33,3,3)

pt = [1,-256,3,4,536]
print(max(pt, key=abs))
print(len(pt))
print(id(2))

print(inspect.getsource(winter))

def sam_range(start,end):
    if start > end:
        start,end = end,start
    return sum(range(start,end + 2 ))

print(sam_range(103,3))


def less(lst):
    return min(lst) * len(lst) + max(lst)

print(less([11,32,53,64,87,1000000]))
pt = {'k1': 'красный',
      'k2': 'черный' ,
      'k3': 'белый' }
pt['near'] = 'person'
pt['r5'] = 'men'

po = pt.get('k1','hello_my_bro')

print(pt.pop('k3'))


#del pt['r5']
for k,y  in pt.items():
    print(f'{k} {y}')

print(pt.keys())

dicts = dict(pt)

print(dicts)

from collections import Counter

p = 'Im like "Python" '
#pl = p.upper()
#pl = p.lower()
#pl = p.replace('I','we')
#pl = p.split(' ')
#pl = p[0]
#pl = p[1]
#pl = p[:10]


def first_last(letter,st):
    first = st.find(letter)
    if first < 0 :
        return None ,None
    last = st.rfind(letter)
    return first, last

sdo = [12,13,11,'wewe',bool,['qwqw']]

pi = sum(filter(lambda x: isinstance (x , int ),sdo ))
print('Сумма чисел',pi)

print(first_last('я',"много етаяяжей в соседнем доме напротив"))

s = 'ewe,ty,kjkj,ooioiiuy'
print(s.split())

text ='''weesdde wwwe wdsdse\n
ree rerkh rerr\n
eree rerer eree\n
ooewi eklsfkl dfddf'''

pt = text.split('\n\n')

ssd = sorted(pt)
print(ssd)

def avemov_fio(fams):
    fams_len = []
    for fio in fams:
        fam = len(fio.split())
        fams_len.append(fam)
    

    min_f, max_f = min(fams_len),max(fams_len)
    avg_f = (min_f + max_f) / 2
    print(int(avg_f))

    for fio in fams:
        if len(fio.split()) == int(avg_f):
            fams.remove(fio)
            break
    return fams
#print(avemov_fio(ssd))

class Trianglechekir:
    def __init__(self,sides):
        self.sides = sides

    def is_triangle(self):
        if all (isinstance (side,(int,float)) for side in self.sides):
            if all(side > 0 for side in self.sides ):
                sorted_sides = sorted(self.sides)
                if sorted_sides[0]+ sorted_sides[1] >sorted_sides[2] :
                    return 'Можно построить треугольник'
                return 'Ничего не выйдет'
            return 'С отрицательными числами нечего не выйдет'
        return 'Нужно вводить только числа'
    
    
point = Trianglechekir([112,113,22])
print(point.is_triangle())

'''pavelAkhtorov'''
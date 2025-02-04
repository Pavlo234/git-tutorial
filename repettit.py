import re 


def to_jaden_case(string):
    # p = ''
    # string = str(string)
    # for i in string:
    #     l = i.title()
    #     p +=l
    return string.title()
    
k = ' pavlo po ,llk po ooo op"kk'

print(to_jaden_case(k))



kl = 'pavlo'
kl = kl.title()

print(kl)




def sum_two_smallest_numbers(numbers):
    # arr = sorted(numbers)
    # return arr[1] + arr[0] 
    return sum(sorted(numbers)[:2]) 


p = [12,1,3,34,212,11,-90]


print(sum_two_smallest_numbers(p))

def who_is_paying(name):
    return [name] if len(name) < 2 else [name, name[0] + name[1]]

# def who_is_paying(name):        
#     return [name, name[0]+name[1]] if len(name) > 2 else [name]




p = 'xspoip'
print(who_is_paying(p))
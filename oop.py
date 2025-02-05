def queue(queuers, pos):
    count = 0
    while queuers[pos] > 0:
        for i in range(len(queuers)):
            if queuers[i] > 0:
                queuers[i] -= 1
                count += 1
                if i == queuers[i] and queuers[pos] == 0:
                    return count

    return count



#     return queuers[pos] 
#     if pos > 0:
#         return queuers

# po = ([1,12,23,1],3 )

print(queue([11,23,45,0,1,3], 0 ))



def countr(n,x):
    count = 0
    while n[x] > 0:
        f = n.pop(0)
        f = f - 1
        if f > 0:
            n.append(f) 
        count += 1
    return count

print(countr([11,12,6,7,34],4))



def countr(n, x):
    count = 0
    while any(value > 0 for value in n)  :  # Проверяем, есть ли элементы > 0 в списке
        f = n.pop(0)  # Берем первый элемент списка
        f -= 1  # Уменьшаем его на 1
        if f > 0:  # Если результат больше 0, добавляем его обратно
            n.append(f)
        count += 1  # Увеличиваем счетчик
    return count



def queue(ticket_counts, friend_index):
    minutes = 0  # Счетчик времени
    while ticket_counts[friend_index] > 0:  # Пока наш друг не получит все билеты
        # Пройдем по всем людям в очереди
        for i in range(len(ticket_counts)):
        # for i in ticket_counts:
            if ticket_counts[i] > 0:
                ticket_counts[i] -= 1  # Уменьшаем количество оставшихся билетов
                minutes += 1  # Увеличиваем время на одну минуту
                # Если это наш друг, проверим, когда он получит все билеты
                if i == friend_index and ticket_counts[i] == 0:
                    return minutes
    return minutes

print(queue([11, 12, 6, 17, 11], 4))
print(queue([1,11, 12, 6], 0))

def number_property(n):
    li = []
    if n < 2:
        li.append(False)
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                li.append(False)
                break
        else:li.append(True)
    if n  % 2 == 0:
        li.append(True)
    else:li.append(False)
    if n % 10 == 0:
        li.append(True)
    else:li.append(False)
    return li
# print(number_property(210))

print((10**0.5))

gitt = 90090
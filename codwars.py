def sum_mul(n, m):
    if n + m <= 2:
        return 'INVALID'
    li = []
    if n <= 0 and m <= 0 or m < 0 or n < 0:
        return 'INVALID'
    else:
        p = range(n,m)
        for i in p:
            if i % n == 0 :
                li.append(i)
    return sum(li)


print(sum_mul(0, 2)) #0

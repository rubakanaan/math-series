def fibonacci(num):
    if num <= 1:
        return num
    else:
        return(fibonacci(num-1) + fibonacci(num-2))


print(fibonacci(9))


def lucas(num):
    a = 2
    b = 1
    if (num == 0):
        return a
    for i in range(2, num + 1):
        c = a + b
        a = b
        b = c

    return b


print(lucas(9))


def sum_series(num, p1=0, p2=1):
    if num == 1:
        return p1
    elif num ==2 :
        return p2
    elif p1 == 0 and p2 == 1:
        return fibonacci(num)
    elif p1 == 2 and p2 == 1:
        return lucas(num)
    else:
        return sum_series(num - 1, p1, p2) + sum_series(num - 2, p1, p2)

print(sum_series(9, 2, 7))

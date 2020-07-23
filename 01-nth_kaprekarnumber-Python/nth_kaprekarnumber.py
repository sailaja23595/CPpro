# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

def karpekar(n):
    if n <= 0:
        return False
    p = n ** 2
    if p < 10:
        if p == n:
            return True
    number = math.ceil(math.log(p,10))
    c = 1
    while c < number:
        number1 = p % 10 ** c
        number2 = p // 10 ** c
        if number1 == 0:
            c = c + 1
            continue
        if number1 + number2 == n:
            return True
            break
        c = c + 1
    return False

def fun_nth_kaprekarnumber(n):
    li = []
    for i in range(79000):
        if karpekar(i):
            li.append(i)
    return li[n]
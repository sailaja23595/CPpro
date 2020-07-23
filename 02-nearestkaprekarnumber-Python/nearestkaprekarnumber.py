# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math
def Kaprekar(n):
    if  n <= 0:
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
def fun_nearestkaprekarnumber(n):
    l = n - math.floor(n)
    h = math.ceil(n) - n
    if Kaprekar(n):
        return n
    number1 = n - l
    number2 = n + h
    while True:
        if Kaprekar(number1):
            if Kaprekar(number2):
                if abs(number1 - n) > abs(number2 - n):
                    return number2
                    break
                else:
                    return number1
                    break
            else:
                return number1
                break
        if Kaprekar(number2):
            return number2
            break
        number1 = number1 -1
        number2 = number2 + 1

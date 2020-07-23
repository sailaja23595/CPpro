# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and 
# nthLeftTruncatablePrime(10) returns 53.



import math

def isPrime(n):
    if n > 1:
        for i in range(2,n):
            if(n%i == 0):
                return False
        return True
    return False

def digitcnt(n):
    n = abs(n)
    c = 1
    while n > 10:
        n = n // 10
        c = c+1
    return c

def leftTruncateprime(n):
    if isPrime(n)== False or str(n). __contains__("0"):
        return False
    else:
        d = digitcnt(n)
        for i in range(1,d):
            p = n % (10 ** i)
            if isPrime(p) == False:
                return False
        return True
def fun_nth_lefttruncatableprime(n):
    li = []
    for i in range(600):
        if leftTruncateprime(i):
            li.append(i)
    return li[n]
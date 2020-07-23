# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

import math

def addition(n):
    add = 0
    while n > 0:
        r = n % 10
        add = add + r
        n = n//10
    return add

def addfactors(n):
    li = []
    while n % 2 == 0 and n > 0:
        li.append(int(2))
        n = n / 2
    for i in range(3,int(math.sqrt(n))+ 1, 2):
        while n % i == 0:
            li.append(int(i))
            n = n / i
    if n > 2:
        li.append(int(n))
    add = 0
    for i in li :
        if len(str(i)) == 1:
            add  = add + i
        elif len(str(i)) > 1 and i is not n:
            add  = add + addition(i)  
    return add

def isprime(n):
    if  n > 1:
        for i in range(2,n):
            if(n % i == 0):
                return False
        return True
    return False

def issmith(n):
    if addition(n) == addfactors(n):
        return True
    else:
        return False

def fun_nth_smithnumber(n):
    l = []
    for i in range(1,500):
        if issmith(i) and not isprime(i):
            l.append(i)
    return l[n]
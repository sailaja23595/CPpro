# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!
def isPrime(n):
    for i in range(2,n):
        if(n%i == 0):
            return False
        else:
            return True 

def ishappynumber(n):
    def sumofsquares(num1):
        add = 0
        while(num1>0):
            r = num1 % 10
            add = add + (r**2)
            num1 = num1 // 10
        return add
    l = []
    while sumofsquares(n) not in l:
        res = sumofsquares(n)
        if res == 1:
            return True
        else:
            l.append(res)
            n = res
    return False

def ishappyprimenumber(n):
    if isPrime(n) and ishappynumber(n):
        return True
    return False

    
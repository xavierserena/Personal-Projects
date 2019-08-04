from math import sqrt
def isPrime(n):
    def isPrimeHelper(x):
        if x > sqrt(n):
            return True
        elif n % x == 0:
            return False
        return isPrimeHelper(x + 1)
    return isPrimeHelper(2)

def printPrimes(n):
    count = 0
    for i in range(2, n):
        if isPrime(i):
            print(i)
            count += 1
    print("There are {} primes between 1 and {}".format(count, n))
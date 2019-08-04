import time
import math

def fib(f, n):
    t = time.time()
    f(n)
    return(time.time() - t)

def comp_fib(n):
    t0, t1 = fib(fast, n), fib(slow, n)
    print('Con memorización es {:1.2f}x más rápido!'.format(t1/t0))

dic = {0:0, 1:1}
def fast(n):
    if n in dic: 
        return dic[n]
    dic[n] = fast(n - 2) + fast(n - 1)
    return dic[n]

def slow(n):
    if n == 0 or n == 1:
        return n
    return slow(n - 2) + slow(n - 1)

def fib(n):
    if n == 0 or n == 1:
        return n
    val = [0] * (n + 1)
    val[1] = 1
    val[2] = 1
    for i in range(3, n + 1):
        val[i] = val[i - 2] + val[i - 1]
    return val[n]

n = 2
while True:
    print("Fib of", n, "is:")
    print(fast(n))
    print()
    n += 100
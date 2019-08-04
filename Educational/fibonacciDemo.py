import time, sys, os

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

def fib(f, n):
    t = time.time()
    print('n:', n)
    print()
    print(f(n))
    # print('Runtime (sec):')
    # return(time.time() - t)

def comp_fib(n):
    blockPrint()
    t0, t1 = fib(fast, n), fib(slow, n)
    enablePrint()
    print('Fast fib is {:1.2f}x faster!'.format(t1/t0))

dic = {0:0, 1:1}
def fast(n):
    if n in dic: 
        return dic[n]
    else:
        dic[n] = fast(n - 2) + fast(n - 1)
        return dic[n]

def slow(n):
    if n == 0: 
        return 0
    elif n == 1:
        return 1 
    else:
        return slow(n - 2) + slow(n - 1)

n = 1000
while True:
    fib(fast, n)
    n += 1000

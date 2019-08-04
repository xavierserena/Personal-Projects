n = 2
memo = [1]
seq = []
value = 1

dic = {0:0, 1:1}
def fib(n):
    if n in dic: 
        return dic[n]
    dic[n] = fib(n - 2) + fib(n - 1)
    return dic[n]

def odd(x):
    return x%2 is not 0

def collatz(x):
    if(x in memo):
        return 1  
    if(x in seq):
        print("Found:", x)
        return 0

    seq.append(x)
    if odd(x):
        value = collatz((3*x + 1)//2)
    else:
        value = collatz(x//2)
    if (value is 1):
        memo.append(x)
        print("Sequence growth:", len(seq))

while value:
    if (n in memo):
        print("Skipped", n)
        print()
    seq = []
    print("Trying:", n)
    print()
    collatz(n)
    n += 1

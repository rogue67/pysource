import time

n = 40

def  fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return  fib(n-1) + fib(n-2)
start = time.time()
fib(n)
stop = time.time()
print("Tid: ", stop - start)

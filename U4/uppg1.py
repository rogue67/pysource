import prog2 
import matplotlib.pyplot as plt
from time import perf_counter as pc

def  fib_py(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return  fib_py(n-1) + fib_py(n-2)

tal = list(range(35,46))
c_tid = []
py_tid = []
for j in tal:
    start = pc()
    prog2.fib(j)
    stop = pc()
    tid = round(stop - start,2)
    print(tid)
    c_tid.append(tid)

for j in tal:
    start = pc()
    fib_py(j)
    stop = pc()
    tid = round(stop - start,2)
    print(tid)
    py_tid.append(tid)

plt.plot(tal,c_tid,'r-',tal,py_tid,'b-')
plt.ylabel('Tid/s')
plt.xlabel('Invärde fib() n')
plt.show()
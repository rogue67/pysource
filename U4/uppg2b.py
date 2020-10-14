import random
import math
import matplotlib.pyplot as plt
import concurrent.futures as cf
from time import perf_counter as pc

antalData_1 = 1_000_000
processer = 10

def randomPoints(n):
    i = 0
    while i < n:
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        yield x,y
        i+=1

def pi_calc(n):
    randomSetSquare = []
    randomSetCircle = []
    for x,y in randomPoints(n):
        if x**2 + y**2 > 1:
            randomSetSquare.append((x,y))
        else:
            randomSetCircle.append((x,y))
    ans = 4*( len(randomSetCircle)/antalData_1 )
    return ans

if __name__== "__main__":

    start = pc()
    with cf.ProcessPoolExecutor() as ex:
        p = [antalData_1]*processer
        resultat = ex.map(pi_calc,p)

        ans = 0
        for r in resultat:
            ans = ans + r
    stop = pc()
    print("Närmevärde för pi  {}".format(ans/processer))
    print("beräkningen tog: {} sekunder".format(stop-start))
import random
import math
import matplotlib.pyplot as plt

randomSetSquare = []
randomSetCircle = []
antalData_1 = 1_000
def randomPoints(n):
    i = 0
    while i < n:
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        yield x,y
        i+=1 

for x,y in randomPoints(antalData_1):

    if x**2 + y**2 > 1:
        randomSetSquare.append((x,y))
    else:
        randomSetCircle.append((x,y))

print("Antal datapunkter:  {}".format(antalData_1))
ans = 4*( len(randomSetCircle)/antalData_1 )
print("Närmevärde för pi: {}".format(ans))
for (X,Y) in randomSetCircle:
    plt.plot(X,Y,'b*')
for (X,Y) in randomSetSquare:
    plt.plot(X,Y,'r*')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
txt = "Närmevärde för pi: " + str(ans)
plt.title(txt)
plt.show()
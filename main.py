from random import randint as rnd
import math
import os
import sys
import time
clear = lambda: os.system("cls")

total = 0
circle = 0
pi = 0
r = 50000

initTime = time.time()
for i in range(r**2):


    x = rnd(-r,r)
    y = rnd(-r,r)
    total +=1

    d = math.sqrt((x**2) + (y**2))

    if d < r:
        circle +=1

    pi = 4 * (circle / total)

    clear()
    print('Total : ' + str(total))
    print('Circle : ' + str(circle)) 
    print('Approximation for Pi : ' + str(pi))

taken = time.time() - initTime
print(str(taken))

    
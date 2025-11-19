import random
import math

def pi(n):
    interior=0
    for i in range(n):
        x=random.random()
        y=random.random()
        if (x-0.5)**2+(y-0.5)**2<=1/4:
            interior+=1
    return 4*(interior/n)

print("pi = ",pi(10000000) )
print(math.pi)


#List Overlap
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
cl = []

for x in b:
    if x in a:
        if x not in cl:
            cl.append(x)
    print(sorted(cl))





rl1 = random.sample(range(1, 50), 15)
print(sorted(rl1))

rl2 = random.sample(range(5, 30), 10)
print(sorted(rl2))

rl3 = []

for l in rl1:
    if l in rl2:
        if l not in rl3:
            rl3.append(l)
    print(sorted(rl3))

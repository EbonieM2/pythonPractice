#Divisors

num = int(input("Please enter a number: "))
divs = list(range(1, 101))
dlist = []

for d in divs:
    if num % d == 0:
        dlist.append(d)
print(dlist)

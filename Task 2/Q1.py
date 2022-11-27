import random

r = random.randint(100, 999)
# print(r) <-- for debugging
hit = 0
miss = 0

while(True):
    r = str(r)
    g = input("Guess a 3-digit number: ")
    for i in range(len(g)):
        if r[i] == g[i]:
            hit += 1
        elif g[i] in r:
            miss += 1
    if hit == 3:
        print("You guessed the number correctly")
        break
    print(hit, "hit", miss, "miss")
    hit = 0
    miss = 0

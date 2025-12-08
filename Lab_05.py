import random
N = 10

def union(r, x, y):
    rx = [x]
    ry = [y]
    if rx != ry:
        for i in range(N):
            if r[i] == ry:
                r[i] = rx

def find(T,L):
    x = 0
    for i in range(N):
        if T[i] == L:
            x = L:
    return x + " in set" + T[i] 


set_r = [i for i in range(N)]
for i in range(N):
    x = random.randrange(N)
    y = random.randrange(N)

    union(set_r, x, y)

for i in range(N):
    find(set_r, i)

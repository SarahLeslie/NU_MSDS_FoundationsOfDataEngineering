import time
import random

def linear(l):
    seen = {}
    dups = 0
    for x in l:
        if x in seen:
            dups +=1
        seen[x] = True
    return dups

def quadratic(l):
    dups = 0
    for x in l:
        for y in l:
            if x == y:
                dups += 1
    dups -= len(l)
    dups /= 2
    return dups

ls = []
for i in [1,100,1000,10000,100000]:
    ls.append([random.randint(0,1000000) for _ in range(i)])

def loop(f,name):
    # new from sarah, next 2 lines below
    dup_results = []
    time_results = []
    for l in ls:
        start = time.time()
        dups = f(l)
        end = time.time()
        #print("%s(%d) took %ss (%d dups)" % (name, len(l), end - start, dups))
        # new from sarah, next 3 lines below
        dup_results.append(dups)
        time_results.append(end - start)
    return dup_results, time_results

loop(linear,"linear")
loop(quadratic,"quadratic")

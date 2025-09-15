from time import perf_counter
start = perf_counter()
import math
#setting initial variables, targetNum is the number of factors we're looking for, n as in "nth triangular number".
targetNum = int(input())
n = 1
listFactors = set()
#using a list here so I can see the factors
while len(listFactors) < targetNum:
    listFactors = set()
    divider=1
    #get triangular number, i chose to use formula over addition. the highest factor with a counterpart will be less than the square root of the initial number.
    triangle = n*(n+1)/2
    while divider <= math.sqrt(triangle):
        if triangle % divider == 0:
            listFactors.add(int(divider))
            listFactors.add(int(triangle/divider))
        divider+=1
    n+=1
print(triangle)
print(listFactors)
stop = perf_counter()
print(f"{stop-start:.7f}")
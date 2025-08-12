import math
#setting initial variables, targetNum is the number of factors we're looking for, n as in "nth triangular number".
targetNum = int(input())
n = 1
listFactors = set()
while len(listFactors) < targetNum:
    listFactors = set()
    divider=1
    triangle = n*(n+1)/2
    while divider <= math.sqrt(triangle):
        if triangle % divider == 0:
            listFactors.add(int(divider))
            listFactors.add(int(triangle/divider))
        divider+=1
    n+=1
print(triangle)
print(listFactors)
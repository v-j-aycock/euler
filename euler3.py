needFactors=int(input())
primeRange=list(range(2,needFactors+1))
composites=set(())
for x in primeRange:
    y=2
    while x*y < needFactors:
        composites.add(x*y)
        y+=1
        if primeRange[-1] % x:
            composites.add(primeRange[-1])
primeRange=[x for x in primeRange if x not in composites]
x=-1
while x>-len(primeRange):
    if needFactors % primeRange[x]==0:
        print(primeRange[x])
        break
    else:
        x-=1

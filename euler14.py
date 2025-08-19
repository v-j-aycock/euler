from time import perf_counter
start=perf_counter()
#startCollatz starts at 2, highestLen to save our highest collatzLen, lenDict to save like 13:10
startCollatz=2
lenDict={}
highestLen = 0
highestStart = 0
while startCollatz < 1000001:
    n=startCollatz
    collatzLen = 1
    while n > 1:
        if n in lenDict:
            collatzLen+=lenDict[n]
            n=1
        elif n % 2 == 0:
            n=n/2
            collatzLen += 1 
        else:
            n=n*3+1
            collatzLen += 1
    lenDict.update({startCollatz:collatzLen})
    if collatzLen > highestLen:
        highestLen = collatzLen
        highestStart = startCollatz
    startCollatz+=1
print(highestLen)
print(highestStart)
stop = perf_counter()
print(f'{stop-start:.7f}')
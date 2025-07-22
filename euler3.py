testPrime=int(input())
primeRange=range(2,testPrime)
#head in the turing sense, our "home" position
rangeHead = 0
def generateMultiples(primeRange, rangeHead):
    rangeIter=primeRange[rangeHead]
    rangeRemove=[]
    nonPrime=0
    #timeRun starts at 1 to skip the first instance of the number
    timeRun=1
    try:
        while nonPrime<testPrime:
            nonPrime=primeRange[(rangeIter*timeRun)]
            rangeRemove.append(nonPrime)
            timeRun+=1
    except: 
        primeRange=[x for x in primeRange if x not in rangeRemove]
        rangeHead+=1
        return primeRange
print(generateMultiples(primeRange,rangeHead))
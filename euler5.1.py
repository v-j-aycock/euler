import prime
#targetNum is the final consecutive divisor we're looking for, x is our divisor test
targetNum = int(input())
x=3
#listPrimes will be used to check powers, currentFactor is the current number divisible consecutively
currentFactor=2
listPrimes=[2]
while x <= targetNum:
    if prime.prime(x) == 1:
        listPrimes.append(x)
        currentFactor = currentFactor*x
    else:
        for y in listPrimes:
            n=1
            while y ** n < x:
                n+=1
            if y ** n == x:
                currentFactor = currentFactor*y
    print(currentFactor)
    x+=1
print(currentFactor)
print(listPrimes)
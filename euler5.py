import sys
#targetNum is the number we're looking for divisors of.
targetNum=int(input())
#setting this in code for simplicity
desiredFactor = 20
factorList = []
#check for factors
x=1
while True:
    while x <= desiredFactor:
        if targetNum % x == 0:
            factorList.append(x)
        x+=1
    print(factorList)
    #check for consecutive factors
    consecFactors = []
    consecFactors.append(factorList[0])
    for x in factorList:
        if factorList[x] == factorList[x-1]+1:
            consecFactors.append(factorList[x])
        else:
            print(targetNum)
            print('Consecutive factors: ',consecFactors)
            break
    targetNum+=desiredFactor
    if len(consecFactors) == 20:
        sys.exit()
    factorList=[]
    x=1
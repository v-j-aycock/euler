#establish variables
fibNum = 1
prevNum = 0
target = 4000000
fibList=[]
#generate list
while fibNum < target:
    holdNum = fibNum
    fibNum = fibNum+prevNum
    prevNum=holdNum
    #check if even
    if fibNum%2 == 0:
        fibList.append(fibNum)
print(sum(fibList))
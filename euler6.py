#establish target number
targetNum=(int(input()))
#generate sum of squares
x=targetNum
squareList=[]
sumList=[]
while x > 0:
    squareList.append(x**2)
    x-=1
sumSquares = sum(squareList)
print('sum of squares: ', sumSquares)
#generate squared sum
x=targetNum
while x > 0:
    sumList.append(x)
    x-=1
squaredSums=(sum(sumList)**2)
print(squareList)
print(sumList)
print('squared sum: ', squaredSums)
print('difference = ', squaredSums-sumSquares)
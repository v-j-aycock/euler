#define variables
targetRange=range(1,1000)
three=3
five=5
divisors = []
#run math
for x in targetRange:
    if x/three == int(x/three):
        divisors.append(x)
    if x/five == int(x/five):
        divisors.append(x)
#clean divisors
singleDivisors=set(list(divisors))
#add and pring
print(sum(singleDivisors))
import prime
import time
start_time = time.time()
x=3
sumPrimes=2
targetNumber = int(input())
while x <= targetNumber:
    if x % 6 != 0:
        if prime.prime(x) == 1:
            sumPrimes+=x
    x+=2
print(sumPrimes)
print("--- %s seconds ---" % (time.time() - start_time))
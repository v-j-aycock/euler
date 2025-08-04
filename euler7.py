import prime
#target prime is the nth prime we're looking for, number primes starts at 2 because our first prime (x) starts at 3. this is so we can iterate by 2.
numberPrimes = 2
targetPrime = int(input())
x=3
currentPrime = 3
while numberPrimes <= targetPrime:
    #see prime.py
    if prime.prime(x) == 1:
        numberPrimes+=1
        currentPrime=x
    x+=2
print(currentPrime)
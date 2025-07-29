#get target number, set x to smallest prime
needFactors=int(input())
x=2
#true loop, breaks when done
while True:
    #checks if needFactors can be evenly divided by x, does it if so. continues
    if needFactors%x == 0:
        needFactors = needFactors/x
        continue
    #checks if needFactors/x is the same. could also be needFactors == x. prints and ends program if so
    if int(needFactors/x) == 1:
        print(int(needFactors))
        break
    #adds 1 to x to iterate through numbers for primes
    x+=1

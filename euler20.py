from time import perf_counter
start = perf_counter()
import math
x=math.factorial(100)
sum=0
for y in str(x):
    sum+=int(y)
print(sum)
stop = perf_counter()
print(f"{stop-start:.7f}")
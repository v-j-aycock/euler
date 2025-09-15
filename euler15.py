from time import perf_counter
start = perf_counter()
import math
n=40
k=20
numerator=math.factorial(n)
denominator= (math.factorial(k)*math.factorial(n-k))
print(numerator/denominator)
stop = perf_counter()
print(f"{stop-start:.7f}")
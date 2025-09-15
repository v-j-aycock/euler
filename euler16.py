from time import perf_counter
start = perf_counter()
longNum = str(2 << 999)
result = 0
#for x in range(len(longNum)):
#    result += int(longNum[x])
print(sum(map(int, longNum)))
stop = perf_counter()
print(f"{stop-start:.7f}")
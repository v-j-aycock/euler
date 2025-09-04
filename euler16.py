longNum = str(2 << 999)
result = 0
#for x in range(len(longNum)):
#    result += int(longNum[x])
print(sum(map(int, longNum)))
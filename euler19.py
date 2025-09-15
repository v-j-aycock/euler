from time import perf_counter
start = perf_counter()
#set variables
year = 1900
sunNum=0
months=[]
leapMonths=[]
day=0
for x in range(12):
    months.append([])
    leapMonths.append([])
for x in range(len(months)):
    if x == 0 or x == 2 or x == 4 or x == 6 or x == 7 or x == 9 or x == 11:
        y = 1
        for n in range(31):
            months[x].append(y)
            leapMonths[x].append(y)
            y+=1
    elif x != 1:
        y = 1
        for n in range(30):
            months[x].append(y)
            leapMonths[x].append(y)
            y+=1
    else:
        y = 1
        for n in range(29):
            months[x].append(y)
            leapMonths[x].append(y)
            y+=1
        months[x].pop()
while year <= 2000:
    if str(year)[-2:] == '00' and year % 400 == 0:
        for x in range(len(leapMonths)):
            for y in range(len(leapMonths[x])):
                if year>1900:
                    if leapMonths[x][y] == 1 and day == 6:
                        sunNum+=1
                        print(x,'/',y,year)
                day+=1
                if day > 6:
                    day=0
    elif str(year)[-2:] != '00' and year % 4 == 0:
        for x in range(len(leapMonths)):
            for y in range(len(leapMonths[x])):
                if year>1900:
                    if leapMonths[x][y] == 1 and day == 6:
                        sunNum+=1
                        print(x,'/',y,year)
                day+=1
                if day > 6:
                    day=0
    else:
        for x in range(len(months)):
            for y in range(len(months[x])):
                if year>1900:
                    if months[x][y] == 1 and day == 6:
                        sunNum+=1
                        print(x,'/',y,year)
                day+=1
                if day > 6:
                    day=0
    year+=1
print(sunNum)
stop = perf_counter()
print(f"{stop-start:.7f}")
numberDict = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
tensDict = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',2:"twenty",3:"thirty",4:'forty',5:"fifty",6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
numberStrngs=[]
for x in range(1,1001):
    n=-1
    for y in str(x):
        print(y)
        try:
            if n == -2:
                if str(x)[n]=='1':
                    numberStrngs.pop()
                    numberStrngs.append(tensDict[int(str(x)[n:])])
                else:
                    numberStrngs.append(tensDict[int(str(x)[n])])
            else:
                numberStrngs.append(numberDict[int(str(x)[n])])
        except:
            numberStrngs.append(numberDict[int(str(x)[n])])
        n-=1
    if len(str(x)) == 3:
        numberStrngs.append('hundredand')
    if len(str(x)) == 4:
        numberStrngs.append('thousand')
print(numberStrngs)
print(sum(len(i) for i in numberStrngs))

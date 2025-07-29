import sys
x=999
y=999

while x>99 and y>99:
    #trueList contains a 1 if str[z] == str[-z] and. will be checked to see if it is the same length as productStr to confirm palindrome. a 0 should break the loop
    trueList=[]
    z=0
    productStr=str(x*y)
    print(productStr)
    while z < int((len(productStr)-1)/2)+1:
        if 0 in trueList:
            z+=20
        elif productStr[z] == productStr[-z-1]:
            trueList.append(1)
            z+=1
            if len(trueList) == int(len(str(productStr))/2):
                print(x,'*',y,'=',x*y)
                sys.exit()
        else:
            trueList.append(0)
            z+=1
    print(trueList)
    if y>=x:
        y-=1
    if x>y:
        x-=1
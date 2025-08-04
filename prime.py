def prime(targetNum):
    import math
    sqrNum = int(math.sqrt(targetNum))
    try:
        while sqrNum > 1:
            if targetNum % sqrNum == 0:
                return 0
            sqrNum-=1
        return 1
    except:
        return 0
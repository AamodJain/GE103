def closestSum(l,k):
    l.sort()
    diff = 1000000
    num = []
    n = len(l)
    i = 0
    j=n-1
    while(i<j):
        s = l[i]+l[j]
        dif = (k-s)
        if(dif==0):
            return [l[i],l[j]]
        if(abs(dif)<=diff):
            diff = abs(dif)
            if(abs(dif)<)
            if(dif>0):
                j-=1
            else:
                i+=1
        

    return num



l = [1,8,3,0,2,4,5] # 0 1 2 3 4 5 8
print(closestSum(l,7))

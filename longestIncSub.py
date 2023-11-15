def longestIncSubSeq(l):
    maxi = []
    n = len(l)
    for i in range(n):
        cur = []
        ele = l[i]
        cur.append(ele)
        for j in range(i+i,n):
            if(l[j]>ele):
                cur.append(l[j])
                ele = l[j]
        if(len(cur)>=len(maxi)):
            maxi = list(cur)
    return maxi

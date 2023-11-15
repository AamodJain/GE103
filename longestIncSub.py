def dict_sort(d):
    l = sorted(list(d.keys()))
    return {i:d[i] for i in l}

def closestSum(l,k):
    l.sort()
    maxSum = l[-1]+l[-2]
    diff_list = {}
    n = len(l)
    i = 0
    j = n-1
    min_diff = abs(k-(l[i]+l[j]))
    num = (l[i],l[j])
    while(i<j):
        curr_diff = (k-(l[i]+l[j]))
        if(abs(curr_diff)<min_diff):
            min_diff = curr_diff
            num = (l[i],l[j])
        if(curr_diff == 0):
            break
        elif(curr_diff<0):
            j-=1
        else:
            i+=1
    return num
    
l = [1,3,4,9,11,20]
s = 18
print(closestSum(l,s))

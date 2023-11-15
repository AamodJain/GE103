def sort(a,b):
    while not a.empty():
        b.push(a.top())
        a.pop()
    
    while not b.empty():
        t=b.top()
        b.pop()

        while not a.empty() and a.top()<t:
            b.push(a.top())
            a.pop()
        a.push(t)
    return a

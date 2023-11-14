class stack:
    def __init__(self):
        self.values = []
    def push(self,d):
        self.values.append(d)
    def pop(self):
        return self.values.pop()
    def top(self):
        return self.values[-1]
    
def paranthesisMatching(s):
    opening_ = '({['
    st = stack()
    for i in s:
        if i in opening_:
            st.push(i)
        else:
            try:
                openp = st.pop()
                #print(i)
                if(d[openp]!=i):
                    return False
            except:
                return False
    if len(st.values):
        return False
    return True

def postfixEval(s):
    op = '+-*/'
    st = stack()
    for i in s:
        if i not in op:
            st.push(i)
        else:
            a = (st.pop())
            b = (st.pop())
            st.push(f'({b}{i}{a})')
    return st.top()

def prefixEval(s):
    op = '+-*/'
    st = stack()
    for i in s[::-1]:
        if i not in op:
            st.push(i)
        else:
            a = (st.pop())
            b = (st.pop())
            st.push(f'({a}{i}{b})')
    return st.top()

        
d = {'(':')','{':'}','[':']'}
#print(paranthesisMatching(input()))
s = input()
#print(postfixEval(s))
print(prefixEval(s))

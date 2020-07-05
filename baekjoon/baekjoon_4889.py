import sys

from collections import deque
read = lambda :sys.stdin.readline().strip()

def check(char):
    q = deque()
    for c in char:
        if len(q)==0 and c=='}':
            q.append('}')
            return False
        if c=='{':
            q.appendleft(c)
        elif c=='}' and q[-1]=='{':
            q.pop()
    if len(q)>0:
        return False

def change(char):
    result = 0
    q = deque()
    i = -1
    for c in char:
        if len(q)==0 and c=='}':
            result+=1
            q.append('{')
            i+=1
        elif c=='{':
            q.append('{')
            i+=1
        elif c=='}' and q[-1]=='{':
            q.pop()
            i-=1
    result+=len(q)//2
    return result

n = 1
while True:
    char = list(read())
    if char[0]=='-':
        break
    if check(char):
        print(str(n)+'. 0')
    else:
        result = change(char)
        print(str(n)+'. '+str(result))
    n+=1


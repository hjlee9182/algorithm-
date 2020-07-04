import sys

from collections import deque
read = lambda :sys.stdin.readline().strip()

n = int(read())
q = deque()
for _ in range(n):
    li = read().split()
    if len(li)==2:
        order,num = li[0],li[1]
        if order=='push':
            q.append(num)
    else:
        order = li[0]
        if order=='pop':
            if len(q)>0:
                print(q.popleft())
            else:
                print(-1)
        elif order=='size':
            print(len(q))
        elif order=='empty':
            if len(q)==0:
                print(1)
            else:
                print(0)
        elif order=='front':
            if len(q)==0:
                print(-1)
            else:
                print(q[0])
        elif order=='back':
            if len(q)==0:
                print(-1)
            else:
                print(q[-1])


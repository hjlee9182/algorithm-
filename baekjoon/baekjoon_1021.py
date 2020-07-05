import sys

from collections import deque
read = lambda :sys.stdin.readline().strip()


n,m = map(int,read().split())

mat = list(map(int,read().split()))
q = deque()
for _ in range(1,n+1):
    q.append(_)
result = 0
for i in mat:
    if i==q[0]:
        q.popleft()
    else:
        index = q.index(i)
        if index<=len(q)//2:
            while i!=q[0]:
                result+=1
                a = q.popleft()
                q.append(a)
        else:
            while i!=q[0]:
                result+=1
                a = q.pop()
                q.appendleft(a)
        q.popleft()
print(result)
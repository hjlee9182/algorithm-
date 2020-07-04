import sys

from collections import deque
read = lambda :sys.stdin.readline().strip()

q = deque()

n = int(read())

for _ in range(1,n+1):
    q.append(_)

while len(q)!=1:
    q.popleft()
    a = q.popleft()
    q.append(a)

print(q[0])
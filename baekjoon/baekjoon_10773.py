import sys

from collections import deque
read = lambda :sys.stdin.readline().strip()

k = int(read())

q = deque()

for _ in range(k):
    n = int(read())
    if n==0:
        q.pop()
    else:
        q.append(n)

print(sum(q))
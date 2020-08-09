import sys
read = lambda :sys.stdin.readline().strip()
from collections import deque
import copy
from collections import defaultdict
import itertools
import math


n = int(read())
mat =[0]
for i in range(n):
    mat.append([])

for i in range(n-1):
    x,y = map(int,read().split())
    mat[x].append(y)
    mat[y].append(x)

visit = [0]*(n+1)
visit[1] = 1
result = [0]*(n+1)

q = deque()
q.append(1)
while len(q)>0:
    num = q.popleft()
    li = mat[num]
    for x in li:
        if visit[x]==0:
            q.append(x)
            visit[x] = 1
            result[x] = num

for i in range(2,n+1):
    print(result[i])


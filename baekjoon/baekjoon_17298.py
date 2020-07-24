import sys
read = lambda :sys.stdin.readline().strip()
from collections import deque
import copy
from collections import defaultdict
import math

n = int(read())
mat = list(map(int,read().split()))
check = [-1]*n
q = deque()
q.append(0)
for i in range(1,len(mat)):
    while len(q)>0:
        a = q[-1]
        if mat[i]>mat[a]:
            check[a] = mat[i]
            q.pop()
        else:
            break
    q.append(i)
for i in q:
    check[i] = -1
print(' '.join(map(str,check)))
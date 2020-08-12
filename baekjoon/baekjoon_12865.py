import sys
read = lambda :sys.stdin.readline().strip()
from collections import deque
import copy
from collections import defaultdict
import itertools
import math

n,k = map(int,read().split())

mat = []
for i in range(n):
    x,y = map(int,read().split())
    mat.append((x,y))

m = [[0 for i in range(k+1)]for j in range(n)]

for i in range(k+1):
    if i>=mat[0][0]:
        m[0][i] =mat[0][1]


for i in range(1,n):
    w,v = mat[i][0],mat[i][1]
    for j in range(k+1):
        if j>=w:
            m[i][j] = max(m[i-1][j],m[i-1][j-w]+v)
        else:
            m[i][j] = m[i-1][j]
print(m[n-1][k])



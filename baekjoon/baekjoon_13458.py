import sys
import math
read = lambda : sys.stdin.readline().strip()
from collections import deque

n = int(read())
mat = list(map(int,read().split()))

b,c = map(int,read().split())

result = 0
for j in range(n):
    now = 0
    value = mat[j]

    now+=1
    value-=b
    if value>0:
        if value%c==0:
            now+=value//c
        else:
            now+=value//c+1

    result+=now
print(result)

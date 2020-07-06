import sys

from collections import deque
read = lambda :sys.stdin.readline().strip()
from itertools import permutations

def check():
    last = len(mat)-1
    while last>0 and mat[last-1]>mat[last]:
        last-=1
    if last==0:
        return []

    target = mat[last-1]
    for i in range(len(mat)-1,last-1,-1):
        if mat[i]>target:
            break
    mat[i],mat[last-1] = mat[last-1],mat[i]
    #print(mat)
    mat2 = mat[:last] + sorted(mat[last:])
    return mat2

n = int(read())
mat = list(map(int,read().split()))
flag = 0
flag2 = 0
li = check()
if len(li)==0:
    print(-1)
else:
    print(' '.join(map(str,li)))
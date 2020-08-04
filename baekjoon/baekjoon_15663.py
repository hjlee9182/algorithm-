import sys
read = lambda :sys.stdin.readline().strip()
from collections import deque
import copy
from collections import defaultdict
import itertools
import math

def dfs(li,num,lis):
    if num==m:
        check = int(''.join(map(str,li.split())).strip())
        if d[check]==0:
            print(li)
            d[check] = 1
        return

    for idx,i in enumerate(lis):
        dfs(li+' '+str(i),num+1,lis[idx+1:])


n,m = map(int,read().split())
mat = list(map(int,read().split()))
mat.sort()
d = defaultdict(int)

for idx,value in enumerate(mat):
    dfs(str(value),1,mat[idx+1:])

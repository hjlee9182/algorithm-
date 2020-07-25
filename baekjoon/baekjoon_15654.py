import sys
read = lambda :sys.stdin.readline().strip()
from collections import deque
import copy
from collections import defaultdict
import itertools
import math

def dfs(visit,li,num):
    if num==m:
        print(li)
        return

    for idx,i in enumerate(mat):
        if visit[idx]==0:
            visit[idx] = 1
            dfs(visit,li+' '+str(i),num+1)
            visit[idx] = 0


n,m = map(int,read().split())
mat = list(map(int,read().split()))
mat.sort()

for idx,value in enumerate(mat):
    check = [0 for i in range(n)]
    check[idx] = 1
    dfs(check,str(value),1)

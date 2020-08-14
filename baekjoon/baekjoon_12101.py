import sys
read = lambda :sys.stdin.readline().strip()
from collections import deque
import copy
from collections import defaultdict
import itertools
import math

def dfs(a,li,result):
    global k_num
    if result==n:
        k_num+=1
        if k_num==k:
            print('+'.join(map(str,li)))
            exit()

    for i in range(1,4):
        if result+i<=n:
            lis = copy.deepcopy(li)
            lis.append(i)
            dfs(i,lis,result+i)



n,k = map(int,read().split())
k_num = 0
for i in range(1,4):
    dfs(i,[i],i)
print(-1)
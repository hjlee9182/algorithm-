import sys
read = lambda :sys.stdin.readline().strip()
from collections import deque
import copy
from collections import defaultdict
import itertools
import math


n,w,l = map(int,read().split())
mat = list(map(int,read().split()))
q = deque()
for i in mat:
    q.append(i)

bridge = [0]*w
total = 0
t = 1
while True:

    if total!=0:
        for i in range(w):
            if bridge[i]!=0:
                if i==0:
                    total-= bridge[i]
                    bridge[i] = 0
                else:
                    bridge[i-1] = bridge[i]
                    bridge[i] = 0

    if total+q[0]<=l:
        bridge[-1] = q.popleft()
        total+=bridge[-1]

    if len(q)==0:
        print(t+w)
        break
    t+=1


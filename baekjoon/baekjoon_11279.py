import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()
import itertools
import copy
import collections
import heapq

mat = []

n = int(read())

for _ in range(n):
    i = int(read())
    if i==0:
        if len(mat)==0:
            print(0)
        else:
            a = heapq.heappop(mat)
            print(-1*a)
    else:
        heapq.heappush(mat,i*-1)
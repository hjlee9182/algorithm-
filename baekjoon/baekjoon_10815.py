import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()
import itertools
import copy
import collections

d = collections.defaultdict(int)
n = int(read())
mat = list(map(int,read().split()))
m = int(read())
li = list(map(int,read().split()))

for i in mat:
    d[i] = 1

for i in li:
    if d[i]==0:
        print(0,end=" ")
    else:
        print(1,end=" ")

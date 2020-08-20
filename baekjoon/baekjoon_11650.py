import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()
import itertools
import copy
import collections


n = int(read())
mat = []
for i in range(n):
    mat.append(list(map(int,read().split())))

mat.sort(key = lambda x : (x[0],x[1]))

for x,y in mat:
    print(f'{x} {y}')
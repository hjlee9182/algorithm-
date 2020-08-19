import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()
import itertools
import copy
import collections


mat = [set() for i in range(51)]
n = int(read())
for i in range(n):
    s = read()
    li = mat[len(s)]
    li.add(s)

for i in range(1,51):
    if len(mat[i])==0:
        continue
    li = list(mat[i])
    li.sort()
    for j in li:
        print(j)



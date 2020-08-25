import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()
import itertools
import copy
import collections

n = int(read())
mat = list(map(int,read().split()))
mat.sort()
print(mat[0]*mat[-1])
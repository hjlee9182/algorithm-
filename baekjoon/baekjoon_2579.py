import sys
import copy
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

t = int(read())
mat = [0]*t
result = [0]*6
for i in range(t):
    mat[i] = int(read())

array = copy.deepcopy(mat)
mat[1] = max(array[0]+array[1],array[1])
mat[2] = max(array[0]+array[2],array[1]+array[2])
for j in range(3,t):
    mat[j] = max(mat[j-3]+array[j]+array[j-1], array[j]+mat[j-2])

print(mat[t-1])

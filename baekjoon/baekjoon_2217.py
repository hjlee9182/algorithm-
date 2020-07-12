import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()
import itertools
import copy

n = int(read())
mat = []
for _ in range(n):
    mat.append(int(read()))

mat.sort()



result = 0
for j in range(n):
    result = max(result,(n-j)*mat[j])
print(result)

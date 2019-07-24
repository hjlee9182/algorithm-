import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

num = int(read())
mat = list(map(int,list(read().split())))
mat.sort()
result = [0]*len(mat)

for i in range(len(mat)):
    if i==0 :
        result[0] = mat[0]
    else : result[i] = mat[i]+result[i-1]

print(sum(result))
import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

t = int(read())
mat =[list(map(int,list(read().split())))for k in range(t)]

result = [[0]*3 for k in range(t)]
result[0] = mat[0]

for i in range(1,t):
    result[i][0] = mat[i][0]+min(result[i-1][1],result[i-1][2])
    result[i][1] = mat[i][1] + min(result[i-1][0], result[i-1][2])
    result[i][2] = mat[i][2] + min(result[i-1][1], result[i-1][0])
print(min(result[t-1]))
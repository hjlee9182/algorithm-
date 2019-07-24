import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

t = int(read())
mat =[list(map(int,list(read().split())))for k in range(t)]
result = [[0]*t for k in range(t)]
result[0] = mat[0]
for i in range(1,t):
    for j in range(len(mat[i-1])):
        if result[i][j] == 0 :
            result[i][j] = mat[i][j]+result[i-1][j]
        else : result[i][j] = max(result[i][j],mat[i][j]+result[i-1][j])
        if result[i][j+1] ==0:
            result[i][j+1] = mat[i][j+1] + result[i - 1][j]
        else: result[i][j+1] = max(result[i][j+1], mat[i][j+1] + result[i - 1][j])

print(max(result[t-1]))


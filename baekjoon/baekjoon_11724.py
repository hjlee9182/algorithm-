import sys
sys.setrecursionlimit(10**6)

def dfs(current):
    global visited
    global mat
    visited[current] = 1
    for i in range(a+1):
        if current==i : continue
        if mat[current][i] ==1 and visited[i]==0 :
            dfs(i)
    return

a,b = map(int,input().split())
mat = [[0]*(a+1) for i in range(a+1)]
for i in range(b):
    x,y = map(int,input().split())
    mat[x][y] = 1
    mat[y][x] = 1
visited = [0]*(a+1)
result = 0
for i in range(a+1):
    if i == 0 : continue
    if visited[i] == 0:
       dfs(i)
       result += 1

print(result)
import sys
from collections import deque
read = lambda : sys.stdin.readline().strip()
import copy

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    global check
    check+=1
    q = deque()
    q.append((x,y))
    mat[x][y] = 0
    result = 1

    while len(q)>0:
        x,y = q.popleft()

        for i in range(4):
            x_ = x+dx[i]
            y_ = y+dy[i]
            if 0<=x_<n and 0<=y_<m:
                if mat[x_][y_]==1:
                    q.append((x_,y_))
                    result+=1
                    mat[x_][y_] = 0
    return result

n,m = map(int,read().split())
check = 0
answer = 0
mat = []
for i in range(n):
    li = list(map(int,read().split()))
    mat.append(li)

for i in range(n):
    for j in range(m):
        if mat[i][j] == 1:
            answer = max(answer, bfs(i,j))
print(check)
print(answer)
import sys

read = lambda :sys.stdin.readline().strip()
import copy
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y,mat):
    q = deque()
    q.append((x,y))
    mat[x][y] = 0

    result = 0

    while len(q)>0:
        x,y = q.popleft()

        for i in range(4):
            x_ = x+dx[i]
            y_ = y+dy[i]
            if 0<=x_<n and 0<=y_<m:
                if mat[x_][y_] == 'L':
                    mat[x_][y_] = mat[x][y]+1
                    result = max(result, mat[x_][y_])
                    q.append((x_,y_))

    return result




n,m = map(int,read().split())
mat =[]
ls = []
for _ in range(n):
    li = list(read())
    mat.append(li)

    for j in range(m):
        if mat[_][j]=='L':
            ls.append((_,j))

result = 0
for x,y in ls:
    mat2 = copy.deepcopy(mat)
    path = bfs(x,y,mat2)
    result = max(result,path)

print(result)

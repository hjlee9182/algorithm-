import sys
from collections import deque
read = lambda : sys.stdin.readline().strip()
import copy

def bfs(x,y,t):
    q = deque()
    q.append((x,y))
    mat[x][y] = t

    while len(q)>0:
        x,y = q.popleft()

        for i in range(4):
            x_ = x+dx[i]
            y_ = y+dy[i]
            if 0<=x_<n and 0<=y_<n:
                if mat[x_][y_]==1:
                    q.append((x_,y_))
                    mat[x_][y_] = t

def bfs2(x,y):
    global answer
    t = mat[x][y]
    q = deque()
    q.append((x,y))
    flag = 0
    visit = []
    while len(q)>0:
        x,y = q.popleft()

        for i in range(4):
            x_ = dx[i]+x
            y_ = dy[i]+y
            if 0<=x_<n and 0<=y_<n:
                if mat[x_][y_]==0:
                    if mat[x][y]<0:
                        mat[x_][y_] = 1
                    else:
                        mat[x_][y_] = mat[x][y]+1
                    q.append((x_,y_))
                    visit.append((x_,y_))
                elif mat[x_][y_]<0 and mat[x_][y_]!=t:
                    answer = min(answer,mat[x][y])
                    flag = 1
                    break
        if flag==1:
            break
    for x,y in visit:
        mat[x][y] = 0
    # print(i,j)
    # for i in range(n):
    #     print(mat2[i])
    # print("_____________________")



answer = 9999999
dx = [0,0,1,-1]
dy = [1,-1,0,0]

n = int(read())
mat = []

for i in range(n):
    mat.append(list(map(int,read().split())))
t = -1
for i in range(n):
    for j in range(n):
        if mat[i][j]==1:
            bfs(i,j,t)
            t = t-1

for i in range(n):
    for j in range(n):
        if mat[i][j]<0:
            bfs2(i,j)
print(answer)

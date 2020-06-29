import sys
from collections import deque
read = lambda : sys.stdin.readline().strip()
import copy

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def check(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        False

def bfs():
    q = deque()
    q.append((0,0))

    while len(q)>0:
        x,y = q.popleft()

        for i in range(4):
            x_ = x+dx[i]
            y_ = y+dy[i]
            if check(x_,y_):
                if visit[x_][y_]==100000000:
                    #가중치가 1이라 append
                    if mat[x_][y_]==1:
                        visit[x_][y_] = visit[x][y]+1
                        q.append((x_, y_))
                    else:#가중치가 0 이라 appendleft
                        visit[x_][y_] = visit[x][y]
                        q.appendleft((x_, y_))

    print(visit[n-1][m-1])


result = 999999999999999999
m,n = map(int,read().split())
mat = []
for i in range(n):
    li = list(read())
    for inx,j in enumerate(li):
        li[inx] = int(j)
    mat.append(li)

visit = [[100000000 for j in range(m)] for i in range(n)]
visit[0][0] = 0
#dfs(0,0,0)
bfs()
#print(result)
import sys
from collections import deque
read = lambda : sys.stdin.readline().strip()
import copy

dx = [0,0,-1,1,-1,-2,-2,-1,1,2,2,1]
dy = [1,-1,0,0,-2,-1,1,2,-2,-1,1,2]
def bfs():
    q = deque()
    q.append((0,0,0,0))
    visit = [[[0 for i in range(m)]for j in range(n)]for e in range(k+1)]

    visit[0][0][0] = 1
    result = 99999999999999
    while len(q)>0:
        x,y,ability,move = q.popleft()

        for i in range(12):
            if ability==k and i>=4:
                break

            x_ = x+dx[i]
            y_ = y+dy[i]

            if 0 <= x_ < n and 0 <= y_ < m:
                if (x_, y_) == (n - 1, m - 1):
                    result = min(result, move + 1)
                elif i>=4:
                    if (visit[ability+1][x_][y_]==0 and mat[x_][y_]==0):
                        q.append((x_, y_, ability + 1, move + 1))
                        visit[ability + 1][x_][y_] = 1
                elif(visit[ability][x_][y_]==0 and mat[x_][y_]==0):
                    q.append((x_, y_, ability, move + 1))
                    visit[ability][x_][y_] = 1

    if result == 99999999999999:
        print(-1)
    else:
        print(result)





k = int(read())
w,h = map(int,read().split())
n,m = h,w
mat = []
for i in range(n):
    mat.append(list(map(int,read().split())))

if (n-1,m-1)==(0,0):
    print(0)
else:
    bfs()
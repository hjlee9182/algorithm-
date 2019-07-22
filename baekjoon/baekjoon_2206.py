import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

def bfs():
    q.append((0,0,0))
    mincount = 100000000
    mat[0][0] = 2
    while q:
        x,y,z = q.popleft()

        for _ in range(4):
            nx = dx[_]+x
            ny = dy[_]+y

            if nx<0 or ny<0 or nx>=n or ny>=m :
                continue
            if z==0 :
                if nx == n - 1 and ny == m - 1:
                    count = visit[x][y] + 2
                    mincount = min(count, mincount)
                if mat[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y] + 1
                    mat[nx][ny] = 2
                    q.append((nx, ny, z))
                if mat[nx][ny] == 1 and z == 0:
                    visit2[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny, 1))
                if mat[nx][ny] == 2 and visit[nx][ny] ==0 :
                    visit[nx][ny] = visit[x][y] + 1
                    mat[nx][ny] = 2
                    q.append((nx, ny, z))
            else:
                if nx == n - 1 and ny == m - 1:
                    count = visit2[x][y] + 2
                    mincount = min(count, mincount)
                if mat[nx][ny] == 0:
                    visit2[nx][ny] = visit2[x][y] + 1
                    mat[nx][ny] = 2
                    q.append((nx, ny, z))
    return mincount



n,m = map(int,read().split())
mat = [list(map(int, list(read()))) for k in range(n)]
visit = [[0]*m for i in range(n)]
visit2 = [[0]*m for i in range(n)]
q = deque()
dx = [0,0,1,-1]
dy = [1,-1,0,0]
if n== 1 and m ==1 :
    print("1")
    sys.exit()

a = bfs()

if a == 100000000 :
    print("-1")
else :
    print(a)
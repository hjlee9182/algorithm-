import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

n,m  = map(int,read().split())
mat = [ list(map(int, list(read()))) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
col  = len(mat[0])-1
row = len(mat)-1
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n -= 1
m -= 1
visit[0][0] = 1
def bfs():
    q = deque()
    q.append((0,0))
    while q:

        a, b = q.popleft()
        if a==n and b ==m:
            print(visit[a][b])
            sys.exit()
        for i in range(4):
            new_x = a+ dx[i]
            new_y = b + dy[i]
            if 0<=new_x<=row and 0<=new_y<=col and mat[new_x][new_y]==1:
                visit[new_x][new_y]  = visit[a][b] +1
                q.append((new_x,new_y))
                mat[new_x][new_y] = -1

print(bfs())
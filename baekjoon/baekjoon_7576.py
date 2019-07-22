import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

n,m = map(int,read().split())

mat = [list(map(int,list(read().split())))for i in range(m)]
q = deque()
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(m):
    for j in range(n):
        if mat[i][j] == 1 :
           q.append((i,j))

def bfs():
    time = 0
    while q :
        time += 1
        qs = len(q)
        while qs > 0:
            x,y = q.popleft()
            for k in range(4):
                nx = dx[k]+x
                ny = dy[k]+y

                if nx<0 or ny<0 or nx>=m  or ny >= n :
                    continue
                if mat[nx][ny] == 0:
                    q.append((nx,ny))
                    mat[nx][ny] = 1
            qs-=1
    return time

t = bfs()

for i in range(m):
    for j in range(n):
        if mat[i][j] == 0 :
            print("-1")
            sys.exit()

print(t-1)
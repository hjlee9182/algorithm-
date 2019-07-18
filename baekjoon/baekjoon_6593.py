import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()


dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs():
    q = deque()
    q.append((sx,sy,sz))

    while q:
        x,y,z = q.popleft()
        if x==ex and y==ey and z == ez:
            print("Escaped in "+str(visit[x][y][z])+" minute(s).")
            return;

        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if 0<=nx<l and 0<=ny<r and 0<=nz<c and (mat[nx][ny][nz] == '.' or mat[nx][ny][nz]=='E') :
                q.append((nx,ny,nz))
                visit[nx][ny][nz] = visit[x][y][z] + 1
                mat[nx][ny][nz] = '!'

    print("Trapped!")




while True:
    l,r,c = map(int,read().split())
    if l==0:
        break;

    visit = [[[0] * c for _ in range(r)] for _ in range(l)]
    mat = [[[] * c for _ in range(r)] for _ in range(l)]
    for i in range(l):
        mat[i] = [ list(map(str, list(read()))) for _ in range(r)]
        read()
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if mat[i][j][k] == 'S' :
                    sx,sy,sz = i,j,k
                if mat[i][j][k] == 'E':
                    ex,ey,ez = i,j,k

    bfs()


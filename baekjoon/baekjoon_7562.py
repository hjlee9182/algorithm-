import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

def move(a,b):
    move_  = [(a+1,b+2),(a+2,b+1),(a-1,b+2),(a-2,b+1),(a+1,b-2),(a+2,b-1),(a-1,b-2),(a-2,b-1)]
    return move_

def bfs():
    q.append((sx,sy))
    while q :
        x, y = q.popleft()
        move_mat = move(x, y)

        for i in range(8):
            nx, ny = move_mat[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= m:
                continue
            if nx == fx and ny == fy:
                print(mat[x][y] + 1)
                return
            if mat[nx][ny] == 0:
                q.append((nx, ny))
                mat[nx][ny] = mat[x][y] + 1




t = int(read())


while t>0:
    m = int(read())
    mat = [[0]*m for k in range(m)]
    sx,sy = map(int,read().split())
    fx,fy = map(int,read().split())
    q = deque()
    if sx == fx and sy ==fy :
        print(0)
        t-=1
        continue
    bfs()
    t-=1

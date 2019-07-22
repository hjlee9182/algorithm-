import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
read = lambda: sys.stdin.readline().strip()

sx, sy= [0] * 2



r, c = map(int, read().split())

mat = [list(map(str, list(read()))) for k in range(r)]
visit = [[0] * c for i in range(r)]
water = deque()

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs():
    q = deque()
    q.append((sx, sy))

    while q:
        ws = len(water)

        while ws > 0:
            x,y = water.popleft()

            for s in range(4):
                nx = dx[s] + x
                ny = dy[s] + y

                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                if mat[nx][ny] == '.' or mat[nx][ny] == '!' or mat[nx][ny] == 'S':
                    water.append((nx, ny))
                    mat[nx][ny] = '*'
            ws -= 1

        qs = len(q)
        while qs > 0:
            x, y = q.popleft()
            for _ in range(4):
                nx = dx[_] + x
                ny = dy[_] + y

                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                if mat[nx][ny] == 'D':
                    print(visit[x][y] + 1)
                    return ;
                if mat[nx][ny] == '.':
                    q.append((nx, ny))
                    mat[nx][ny] = '!'
                    visit[nx][ny] = visit[x][y] + 1
            qs -= 1

    print("KAKTUS")


for i in range(r):
    for j in range(c):

        if mat[i][j] == 'S':
            sx, sy = i, j
        if mat[i][j] == '*':
            water.append((i, j))

bfs()
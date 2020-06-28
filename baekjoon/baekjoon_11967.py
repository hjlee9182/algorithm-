import sys
from collections import deque
read = lambda : sys.stdin.readline().strip()
import copy

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    global light

    nvisit = [[0 for i in range(n)]for j in range(n)]

    nvisit[0][0] = 1
    q = deque()
    q.append((0,0))
    result = 1
    nvisit[0][0] = 1
    while len(q)>0:

        x,y = q.popleft()


        for a,b in mat[x][y]:
            light.add((a,b))
            bright[a][b] = 1

        for i in range(4):
            x_ = x+dx[i]
            y_ = y+dy[i]

            if 0<=x_<n and 0<=y_<n:
                if nvisit[x_][y_]==0 and bright[x_][y_]==1 :
                    nvisit[x_][y_] = 1
                    q.append((x_,y_))



n,m = map(int,read().split())

mat = [[[] for i in range(n)]for j in range(n)]
visit = [[0 for i in range(n)]for j in range(n)]
bright = [[0 for i in range(n)] for j in range(n)]
bright[0][0] = 1



for _ in range(m):
    x,y,a,b = map(int,read().split())
    mat[x-1][y-1].append((a-1,b-1))

light = set()
light.add((0,0))
while True:
    l = len(light)
    bfs()
    if len(light)==l:
        print(len(light))
        break

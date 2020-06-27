import sys
from collections import deque
read = lambda : sys.stdin.readline().strip()
import copy
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def ispossible(li):

    q = li
    x1,y1 = bird[1]
    rq = deque()
    while len(q)>0:
        x,y = q.popleft()

        for i in range(4):
            x_ = x+dx[i]
            y_ = y+dy[i]
            if 0<=x_<n and 0<=y_<m:
                if (x_,y_)==(x1,y1):
                    return []
                if mat[x_][y_]=='.' and visit[x_][y_]==0:
                    q.append((x_,y_))
                    visit[x_][y_] = 1
                elif mat[x_][y_]=='X'and visit[x_][y_] == 0:
                    rq.append((x_,y_))
                    visit[x_][y_] = 1
    return rq

def check(x,y):
    for i in range(4):
        x_ = x + dx[i]
        y_ = y + dy[i]
        if 0 <= x_ < n and 0 <= y_ < m:
            if mat[x_][y_]=='.'or mat[x_][y_]=='L':
                return True
    return False


n,m = map(int,read().split())

mat = []
bird = []
ice = deque()
for i in range(n):
    li = list(read())
    mat.append(li)
    for j in range(m):
        if mat[i][j]=='L':
            bird.append((i,j))
            ice.append((i,j))
        if mat[i][j]=='.':
            ice.append((i,j))

visit = [[0 for i in range(m)] for j in range(n)]
day =0
l = deque()
mat[bird[0][0]][bird[0][1]] = 1
l.append((bird[0][0],bird[0][1]))
while True:

    rq = ispossible(l)
    if rq==[]:
        print(day)
        break
    day+=1

    l = rq
    s = len(ice)
    for _ in range(s):
        x,y = ice.popleft()

        for i in range(4):
            x_ = dx[i]+x
            y_ = dy[i]+y
            if 0<=x_<n and 0<=y_<m:
                if mat[x_][y_]=='X':
                    ice.append((x_,y_))
                    mat[x_][y_] = '.'


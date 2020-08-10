import sys
read = lambda :sys.stdin.readline().strip()
from collections import deque
import copy
from collections import defaultdict
import itertools
import math

def check():
    q = deque()
    for i in range(r):
        for j in range(c):
            if mat[i][j]=='.':
                q.append((i,j))
            mat[i][j] = 'O'
    return q

r,c,n = map(int,read().split())

mat = []
q = deque()
for i in range(r):
    li = list(read())
    mat.append(li)
    for j,b in enumerate(li):
        if b=='O':
            q.append((i,j))

t = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]
flag = 0
while(t<n):
    t+=1
    if flag ==0:
        q2 = check()
        flag = 1
    elif flag==1:
        remove = []
        while len(q)>0:
            x,y = q.popleft()
            if mat[x][y]=='.':
                continue
            mat[x][y] = '.'
            remove.append((x,y))
            for i in range(4):
                x_ = x+dx[i]
                y_ = y+dy[i]
                if 0<=x_<r and 0<=y_<c:
                    remove.append((x_,y_))
        for x,y in remove:
            mat[x][y] = '.'
        while len(q2)>0:
            x,y  = q2.popleft()
            if mat[x][y]=='O':
                q.append((x,y))
        flag = 0

for i in range(r):
    print(''.join(mat[i]))
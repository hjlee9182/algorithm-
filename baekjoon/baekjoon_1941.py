import sys
read = lambda :sys.stdin.readline().strip()
from collections import deque
import copy
from collections import defaultdict
import itertools

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def check(li):
    global c
    for x,y in li:
        c[x][y] = 1
    q = deque()
    q.append((li[0][0],li[0][1]))
    c[li[0][0]][li[0][1]] = 0
    while len(q)>0:
        x,y = q.popleft()

        for i in range(4):
            x_ = x+dx[i]
            y_ = y+dy[i]
            if 0<=x_<5 and 0<=y_<5:
                if c[x_][y_]==1:
                    q.append((x_,y_))
                    c[x_][y_] = 0
    num = 0
    for x, y in li:
        if c[x][y]==1:
            num+=1
        c[x][y] = 0
    if num==0:
        return True
    else:
        return False


group = []
visit = []
c = [[0 for i in range(5)]for j in range(5)]
for i in range(5):
    for j in range(5):
        visit.append((i,j))

result = 0
mat = []
for i in range(5):
    mat.append(list(read()))

for li in list(itertools.combinations(visit,7)):
    #print(li)
    s = 0
    lim = 0
    for (x,y) in li:
        if mat[x][y]=='S':
            s+=1
        else:
            lim+=1
    if s>=4:
        if check(li):
            result+=1
print(result)


import sys
read = lambda :sys.stdin.readline().strip()
from collections import deque
import copy
from collections import defaultdict
import itertools
import math

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def check(mat):
    for i in range(n):
        for j in range(n):
            if mat[i][j]==-1:
                return False
    return True

def bfs(virus,mat):

    t = 0
    while len(virus)>0:
        now = len(virus)
        if check(mat):
            return t

        for i in range(now):
            x,y = virus.popleft()
            time = mat[x][y]
            for i in range(4):
                x_ = x+dx[i]
                y_ = y+dy[i]
                if 0<=x_<n and 0<=y_<n:
                    if mat[x_][y_] == -1:
                        mat[x_][y_] = time+1
                        virus.append((x_,y_))
        t+=1

    if check(mat):
        return t
    else:
        return -1



n,m = map(int,read().split())

mat = []
# -2 벽 -1 빈칸 0 바이러스
d = {0:-1,1:-2,2:-1}
v =[]
for i in range(n):
    li = list(map(int,read().split()))
    for idx,j in enumerate(li):
        if j==2:
            v.append((i,idx))
    li = list(map(lambda x : d[x],li))
    mat.append(li)
result = 10000

for li in list(itertools.combinations(v,m)):
    mat2 = copy.deepcopy(mat)
    q = deque()
    for x,y in li:
        mat2[x][y] = 0
        q.append((x,y))
    value = bfs(q,mat2)
    if value!=-1:
        result = min(value,result)

if result==10000:
    print(-1)
else:
    print(result)

#bfs()



import sys

read = lambda :sys.stdin.readline().strip()
from collections import deque

dx =[0,0,1,-1]
dy = [1,-1,0,0]
def bfs():
    visit = [[0 for i in range(n)]for j in range(n)]
    q = deque()
    q.append((0,0,0))
    visit[0][0] = 1
    while len(q)>0:
        x,y,num = q.popleft()

        for i in range(4):
            x_ = x+dx[i]
            y_ = y+dy[i]
            if 0<=x_<n and 0<=y_<n:
                if visit[x_][y_]==0:
                    if (x_,y_)==(n-1,n-1):
                        return num
                    if mat[x_][y_] == 1:
                        q.appendleft((x_,y_,num))
                        #visit[x_][y_] = min(visit[x_][y_],num)
                    else:
                        q.append((x_,y_,num+1))
                        #visit[x_][y_] = min(visit[x_][y_],num+1)
                    visit[x_][y_] = 1
    print(visit)
    #return visit[n-1][n-1]

n = int(read())

mat =[]
for i in range(n):
    li = list(map(int,read()))
    mat.append(li)

print(bfs())

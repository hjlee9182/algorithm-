import sys
read = lambda :sys.stdin.readline().strip()
from collections import deque
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
dir_c = [0,2,1,4,3]
class horse:

    def __init__(self,x,y,dir):
        self.dir = dir
        self.x = x
        self.y = y
    def move(self):
        return self.x+dx[self.dir],self.y+dy[self.dir]
    def set_position(self,x,y):
        self.x = x
        self.y = y

n ,k = map(int,read().split())
color = []
for i in range(n):
    color.append(list(map(int,read().split())))
mat = [[[] for i in range(n)]for j in range(n)]

q = deque()
for i in range(k):
    x,y,z = map(int,read().split())
    h = horse(x-1,y-1,z)
    mat[x-1][y-1].append(h)
    q.append(h)
result = 0
for i in range(len(mat)):
    print(mat[i])
print("_______________________________")
while True:
    if result>=1000:
        print(-1)
        break
    result+=1
    for _ in range(k):
        h = q.popleft()
        n_x,n_y = h.x,h.y
        line = mat[n_x][n_y]
        index = line.index(h)
        x,y = h.move()
        if (x<0 or x>=n or y<0 or y>=n):
            h.dir = dir_c[h.dir]
            x,y = h.move()

        if 0<=x<n and 0<=y<n:
            if color[x][y]==2:
                h.dir = dir_c[h.dir]
                x, y = h.move()
            if 0 <= x < n and 0 <= y < n:
                if color[x][y]==0:
                    for i in range(index,len(line)):
                        line[i].set_position(x,y)
                        mat[x][y].append(line[i])
                    mat[n_x][n_y] = mat[n_x][n_y][:index]
                elif color[x][y]==1:
                    for i in range(len(line)-1,index-1,-1):
                        line[i].set_position(x,y)
                        mat[x][y].append(line[i])
                    mat[n_x][n_y] = mat[n_x][n_y][:index]
        q.append(h)
        if 0<=x<n and 0<=y <n:
            if len(mat[x][y])>=4:
                print(result)
                exit()
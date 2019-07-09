import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    num=1
    mat[x][y] = 0
    for q in range(4):
        new_x = dx[q] + y
        new_y = dy[q] + x
        if 0<=new_x<b and 0<=new_y<a and mat[new_y][new_x]==1:
           num += dfs(new_y,new_x)
    return num

a,b,c = map(int,input().split())
dx =[0,0,1,-1]
dy= [1,-1,0,0]
mat = [[0]*b for _ in range(a)]

for _ in range(c):
    x,y = map(int,input().split())
    mat[x-1][y-1] = 1;

ma = 0
for i in range(a):
    for j in range(b):
        if mat[i][j] == 1:
            result = dfs(i,j)
            ma = max([result,ma])
print(ma)
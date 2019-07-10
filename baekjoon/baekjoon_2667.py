import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()
def dfs(x,y):
    size=1
    mat[x][y] = 0
    for i in range(4):
        new_x = dx[i] + x
        new_y= dy[i] + y
        if(0<=new_x<num and 0<=new_y<num and mat[new_x][new_y]==1):
          size+=  dfs(new_x,new_y)
    return size

dx = [0,0,1,-1]
dy = [1,-1,0,0]
num = int(input())
li = []

mat = [ list(map(int, list(read()))) for _ in range(num)]

for i in range(num):
    for j in range(num):
        if mat[i][j] == 1 :
            result = dfs(i,j)
            li.append(result)

print(len(li))
li.sort()
for i in range(len(li)):
    print(li[i])
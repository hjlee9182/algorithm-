import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

def dfs(x,y) :
    mat[x][y] = 1
    size=1
    for i in range(4):
        new_x = dx[i]+x
        new_y = dy[i]+y
        if 0<=new_x<m and 0<=new_y<n and mat[new_x][new_y]==0 :
          size+=  dfs(new_x,new_y)

    return size

m,n,k = map(int,read().split())

dx= [0,0,1,-1]
dy = [1,-1,0,0]
mat = [[0]*n  for _ in range(m)]
li = []
for _ in range(k):
    x1,y1,x2,y2 = map(int,read().split())

    for i in range(y1,y2):
        for j in range(x1,x2) :
            mat[i][j] = 1

for i in range(m):
    for j in range(n):
        if mat[i][j] ==0:
            result = dfs(i,j)
            li.append(result)

li.sort()
print(len(li))
st=""
for _ in range(len(li)):
   if _ == 0 :
       st += str(li[_])
   else:
       st+= " "+str(li[_])

print(st)
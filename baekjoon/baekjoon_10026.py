import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

def dfs(x,y) :
    mat[x][y] = 1
    for i in range(4):
        new_x = dx[i]+x
        new_y = dy[i]+y
        if 0<=new_x<num and 0<=new_y<num and mat[new_x][new_y]==0 :
            dfs(new_x,new_y)

def b_dfs(x,y) :
    mat[x][y] = 1
    for i in range(4):
        new_x = dx[i]+x
        new_y = dy[i]+y
        if 0<=new_x<num and 0<=new_y<num and mat[new_x][new_y]== 'B' :
            b_dfs(new_x,new_y)

def r_dfs(x,y) :
    mat[x][y] = 0
    for i in range(4):
        new_x = dx[i]+x
        new_y = dy[i]+y
        if 0<=new_x<num and 0<=new_y<num and mat[new_x][new_y]=='R' :
            r_dfs(new_x,new_y)

def g_dfs(x,y) :
    mat[x][y] = 0
    for i in range(4):
        new_x = dx[i]+x
        new_y = dy[i]+y
        if 0<=new_x<num and 0<=new_y<num and mat[new_x][new_y]=='G' :
            g_dfs(new_x,new_y)

num = int(input())
li = []

mat = [ list(map(str, list(read()))) for _ in range(num)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
blue = 0
red=0
green=0
rgr= 0
for i in range(num):
    for j in range(num):
        if mat[i][j] == 'B':
            b_dfs(i,j)
            blue +=1
        elif mat[i][j] == 'R':
            r_dfs(i,j)
            red += 1
        elif mat[i][j] == 'G':
            g_dfs(i,j)
            green += 1

for i in range(num):
    for j in range(num):
        if mat[i][j]== 0 :
            dfs(i,j)
            rgr+=1

result1 = blue+green+red
result2 = blue+rgr
st = str(result1)+" "+str(result2)
print(st)
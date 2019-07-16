import sys
import copy
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()


def dfs(x,y,h):
    mat2[x][y] = -1
    for q in range(4):
        new_x = dx[q]+x
        new_y = dy[q]+y
        if 0<=new_x<num and 0<=new_y<num and mat2[new_x][new_y]>h :
            dfs(new_x,new_y,h)

num= int(read())

maxnum = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
mat = [ list(map(int, list(read().split(' ')))) for _ in range(num)]

for _ in range(num):
    maxnum = max(maxnum, max(mat[_]))

max1=0
result = 0
for w in range(maxnum):
    result = 0
    mat2 = copy.deepcopy(mat)
    for i in range(num):
        for j in range(num):
            if mat2[i][j] > w:
                dfs(i,j,w)
                result+=1

    max1 = max(max1,result)

print(max1)
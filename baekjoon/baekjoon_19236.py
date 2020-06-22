import sys
import itertools
read = lambda : sys.stdin.readline().strip()
import copy

def dfs(shark,mat,fish,summ):
    global result
    for j in range(len(fish)):
        number, d, x, y  = fish[j][0],fish[j][1],fish[j][2],fish[j][3]
        if number==0:
            continue
        for i in range(8):
            x_ = dx[(d+i)%8]+x
            y_ = dy[(d+i)%8]+y
            if 0<=x_<4 and 0<=y_<4:
                if mat[x_][y_]>0:
                    target = mat[x_][y_]
                    fish[j][2],fish[j][3],fish[target][2],fish[target][3]=fish[target][2],fish[target][3],fish[j][2],fish[j][3]
                    mat[x][y],mat[x_][y_] = target,number
                    fish[j][1] = (d + i) % 8
                    break
                if mat[x_][y_]==0:
                    fish[j][2],fish[j][3] = x_,y_
                    mat[x][y] = 0
                    mat[x_][y_] = number
                    fish[j][1] = (d+i)%8
                    break

    d,x,y = shark
    for i in range(1,5):
        x_ = x+dx[d]*i
        y_ = y+dy[d]*i
        if 0<=x_<4 and 0<=y_<4:
            if mat[x_][y_]>0:

                target = mat[x_][y_]
                s2 = copy.deepcopy(shark)
                fish2 = copy.deepcopy(fish)
                mat2 = copy.deepcopy(mat)
                s2[0] = fish2[target][1]
                s2[1],s2[2] = x_,y_
                fish2[target][0] = 0
                mat2[x_][y_] = -1
                mat2[x][y] = 0

                dfs(s2,mat2,fish2,summ+target)

    result = max(result,summ)
    return



result = 0
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
mat = []
fish = [[0,0,0,0]]
for i in range(4):
    l = list(map(int,read().split()))
    value = []
    for j in range(0,8,2):
        value.append(l[j])
        fish.append([l[j],l[j+1]-1,i,j//2])
    mat.append(value)
fish.sort()
first = mat[0][0]
fish[first][0] = 0
shark = [fish[first][1],0,0]
mat[0][0] = -1

dfs(shark,mat,fish,first)
print(result)
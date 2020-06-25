import sys
from collections import deque
read = lambda : sys.stdin.readline().strip()
import copy
def p():
    print("this is map")
    for i in range(n):
        print(mat2[i])
    print("_____________________")
    print("this is smell")
    for i in range(n):
        print(mat_s[i])
    print("_____________________")
def clean(mat):
    global shark
    for i in range(n):
        for j in range(n):
            s = mat[i][j]
            if s==[0,0]:
                continue
            t = s[1]-1
            if t==0:
                mat[i][j] = [0,0]
            else:
                mat[i][j][1]=t
    for i in range(1,m+1):
        s = shark[i]
        if s==0:
            continue
        else:
            mat[s[0]][s[1]] = [i,k]
def check(mat):
    for i in range(n):
        for j in range(n):
            if mat[i][j]>1:
                return False
    return True

dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]
n,m,k = map(int,read().split())

mat = []
shark = dict()
for i in range(n):
    li = list(map(int,read().split()))
    mat.append(li)
    for j in range(n):
        if mat[i][j]>0:
            shark[mat[i][j]] = (i,j)

direction = list(map(int,read().split()))
direction.insert(0,0)
s_d = [[]]
for i in range(m):
    li = [[]]
    for j in range(4):
        li.append(list(map(int,read().split())))
    s_d.append(li)
mat_s = [[[0,0] for i in range(n)]for j in range(n)]
t = 0

for i in range(1,m+1):
    x,y = shark[i]
    mat_s[x][y] = [i,k]

while True:
    t+=1
    #print(direction)
    smell_check = [[] for i in range(m+1)]
    mat2 = [ [0 for i in range(n)]for j in range(n)]
    for _ in range(1,m+1):
        s = shark[_]
        if s == 0:
            continue
        number = _
        x,y = s[0],s[1]
        smell_check[number] = [x,y]
        d = direction[number]
        now_d = s_d[number][d]
        flag = 0
        smell = []
        for j in now_d:
            x_ = dx[j]+x
            y_ = dy[j]+y
            if 0<=x_<n and 0<=y_<n:
                if mat[x_][y_]==0 and mat_s[x_][y_]==[0,0]:
                    flag = 1
                    if mat2[x_][y_]!=0:
                        target = mat2[x_][y_]
                        if target>number:
                            shark[target] = 0
                            mat2[x_][y_] = number
                            shark[number] = (x_,y_)
                            direction[number] = j
                        else:
                            shark[number] = 0
                    else:
                        shark[number] = (x_,y_)
                        mat2[x_][y_] = number
                        direction[number] = j
                    break
                elif mat[x_][y_]>0:
                    continue
                elif mat_s[x_][y_][0]==number:
                    smell.append([(x_,y_),j])

        if flag==0 and len(smell)>0:
            x_,y_ = smell[0][0]
            mat2[x_][y_] = number
            shark[number] = (x_,y_)
            direction[number] = smell[0][1]
            fx,fy = x_,y_
    clean(mat_s)
    #p()
    if check(mat2):
        print(t)
        break
    if t>=1000:
        print(-1)
        break
    mat = mat2
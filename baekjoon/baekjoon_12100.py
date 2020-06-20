import sys
import math
read = lambda : sys.stdin.readline().strip()
from collections import deque
import copy
def move(mat,visit,dir):
    if dir==0:
        for i in range(1,n):
            for j in range(n):
                if mat[i][j]!=0:
                    target = i
                    for t in range(i):
                        if ((mat[target-1][j] == mat[i][j]) and visit[target-1][j] ==0) \
                                or mat[target-1][j]==0:
                            target-=1
                            if target==0:
                                break
                            continue
                        break
                    if target!=i:
                        if (mat[target][j] == mat[i][j]) and visit[target][j] ==0:
                            mat[target][j] = mat[i][j]*2
                            visit[target][j] = 1
                            mat[i][j] = 0
                        elif mat[target][j]==0:
                            mat[target][j] = mat[i][j]
                            mat[i][j] = 0
    elif dir==1:
        for j in range(n-2,-1,-1):
            for i in range(n):
                if mat[i][j]!=0:
                    target = j
                    for t in range(n-1):
                        if ((mat[i][target+1]==mat[i][j]) and visit[i][target+1]==0)\
                                or mat[i][target+1]==0:
                            target+=1
                            if target==n-1:
                                break
                            continue
                        break
                    if target!=j:
                        if (mat[i][target]==mat[i][j]) and visit[i][target]==0:
                            mat[i][target] = mat[i][j]*2
                            visit[i][target] = 1
                            mat[i][j] = 0
                        elif mat[i][target]==0:
                            mat[i][target] = mat[i][j]
                            mat[i][j] = 0
    elif dir==2:
        for i in range(n-2,-1,-1):
            for j in range(n):
                if mat[i][j]!=0:
                    target = i
                    for t in range(n-1):
                        if ((mat[target+1][j] == mat[i][j]) and visit[target+1][j] ==0)\
                                or mat[target+1][j]==0:
                            target+=1
                            if target==n-1:
                                break
                            continue
                        break
                    if target!=i:
                        if (mat[target][j] == mat[i][j]) and visit[target][j] ==0:
                            mat[target][j] = mat[i][j]*2
                            visit[target][j] = 1
                            mat[i][j] = 0
                        elif mat[target][j] == 0:
                            mat[target][j] = mat[i][j]
                            mat[i][j] =0
    elif dir==3:
        for j in range(1,n):
            for i in range(n):
                if mat[i][j] != 0:
                    target = j
                    for t in range(j):
                        if (mat[i][target-1] == mat[i][j]) and visit[i][target-1] == 0\
                                or mat[i][target-1]==0:
                            target-=1
                            if target==0:
                                break
                            continue
                        break
                    if target!=j:
                        if (mat[i][target] == mat[i][j]) and visit[i][target] == 0:
                            mat[i][target] = mat[i][j] * 2
                            visit[i][target] = 1
                            mat[i][j] = 0
                        elif mat[i][target]==0:
                            mat[i][target] = mat[i][j]
                            mat[i][j] = 0

def dfs(num,m):
    global result
    if num==5:
        for i in range(n):
            result = max(result,max(m[i]))
        return


    for i in range(4):
        m2 = []
        for j in range(n):
            a = copy.copy(m[j])
            m2.append(a)
        visit = [[0 for q in range(n)] for k in range(n)]
        move(m2, visit, i)

        dfs(num + 1, m2)


result = 0
n = int(read())
mat = []
for i in range(n):
    mat.append(list(map(int,read().split())))

dfs(0,mat)
print(result)
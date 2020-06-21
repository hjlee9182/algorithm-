import sys
read = lambda : sys.stdin.readline().strip()
import copy
import itertools

n,m,t = map(int,read().split())
mat = []
for i in range(n):
    mat.append(list(map(int,read().split())))
for _ in range(t):
    x,d,k = map(int,read().split())

    for i in range(n):
        if (i+1)%x==0:
            if d==0:
                for q in range(k):
                    last = mat[i].pop(len(mat[i])-1)
                    mat[i].insert(0,last)
            else:
                for q in range(k):
                    first = mat[i].pop(0)
                    mat[i].append(first)
    check = []
    flag = 0
    zero_num = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j]==0:
                zero_num+=1
                continue


            if j==0:
                if mat[i][j]==mat[i][m-1]:
                    check.append((i,m-1))
                if mat[i][j]==mat[i][1]:
                    check.append((i,1))
            elif 1<=j<=m-2:
                if mat[i][j]==mat[i][j-1]:
                    check.append((i,j-1))
                if mat[i][j]==mat[i][(j+1)]:
                    check.append((i,(j+1)))
            elif j==m-1:
                if mat[i][j]==mat[i][0]:
                    check.append((i,0))
                if mat[i][j]==mat[i][m-2]:
                    check.append((i,m-2))
            if i==0:
                if mat[i][j]==mat[1][j]:
                    check.append((1,j))
            elif 1<=i<=n-2:
                if mat[i-1][j]==mat[i][j]:
                    check.append((i-1,j))
                if mat[(i+1)][j]==mat[i][j]:
                    check.append(((i+1),j))
            elif i==n-1:
                if mat[n-1][j]==mat[n-2][j]:
                    check.append(((n-2,j)))

    for x_,y_ in check:
        mat[x_][y_] = 0
    if len(check)==0:
        summ= 0
        for i in range(n):
            summ+=sum(mat[i])
        if n*m-zero_num==0:
            avg = 0
        else:
            avg = summ/(n*m-zero_num)
        for i in range(n):
            for j in range(m):
                if mat[i][j]!=0:
                    if mat[i][j]>avg:
                        mat[i][j] -=1
                    elif mat[i][j]<avg:
                        mat[i][j] +=1

result = 0
for i in range(n):
    result+=sum(mat[i])
print(result)
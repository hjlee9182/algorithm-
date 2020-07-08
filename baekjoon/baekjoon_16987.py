import sys
from collections import deque
read = lambda : sys.stdin.readline().strip()
import copy
import collections

def dfs(number):
    global answer
    if number>=n:
        result = 0
        for i in range(n):
            if mat[i][0]<=0:
                result+=1
        answer = max(answer,result)
        return
    elif mat[number][0]<=0:
        dfs(number+1)
    else:
        flag = 0
        for i in range(n):
            if i==number or mat[i][0]<=0:
                continue
            mat[number][0] -=mat[i][1]
            mat[i][0] -=mat[number][1]
            flag = 1
            dfs(number+1)
            mat[number][0]+=mat[i][1]
            mat[i][0] +=mat[number][1]
        if flag==0:
            dfs(n)




answer = 0
n = int(read())
mat = []
for _ in range(n):
    mat.append(list(map(int,read().split())))

dfs(0)
print(answer)
import sys
read = lambda : sys.stdin.readline().strip()

def dfs(st,num,li):
    if num==m:
        print(st)
        return

    for idx,value in enumerate(li):
        dfs(st+' '+str(value),num+1,li[idx+1:])

n,m = map(int,read().split())

mat = list(map(int,read().split()))

mat.sort()

if n==m:
    print(' '.join(map(str,mat)))
else:
    start = 0
    while start+m<=n:
        li = mat[start+1:]
        #visit = [0]*mat
        dfs(str(mat[start]),1,li)
        start+=1

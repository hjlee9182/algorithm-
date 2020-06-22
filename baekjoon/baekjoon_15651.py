import collections
import sys
read = lambda : sys.stdin.readline().strip()
import itertools

def dfs(num,st):
    if num==m:
        print(st)
        return

    for i in mat:
        if num==m-1:
            dfs(num+1,st+str(i)+' ')
        else:
            dfs(num+1,st+str(i)+' ')


n,m = map(int,read().split())

mat = [i for i in range(1,n+1)]

#dfs(0,'')
li = list(itertools.product(mat,repeat=m))
for i in range(len(li)):
    st = ''
    for j in li[i]:
        st+=str(j)+' '
    print(st)

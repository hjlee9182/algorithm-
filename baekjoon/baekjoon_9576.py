import sys
import collections
read = lambda : sys.stdin.readline().strip()

t = int(read())
for _ in range(t):
    n,m = map(int,read().split())
    min_d = collections.defaultdict(int)
    min_result=0
    mat = []
    for __ in range(m):
        s,l = map(int,read().split())
        mat.append((s,l))
    mat = sorted(mat,key = lambda x : x[1])
    for k in range(m):
        s,l = mat[k]
        for i in range(s,l+1):
            if min_d[i]==0:
                min_result+=1
                min_d[i] = 1
                break

    print(min_result)



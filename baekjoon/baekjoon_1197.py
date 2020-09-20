
import sys
read = lambda :sys.stdin.readline().strip()

def find(x):
    if d[x]==x:
        return x
    else:
        root = find(d[x])
        d[x] = root
        return root

def union(a,b):
    a_root = find(a)
    b_root = find(b)
    if a_root!=b_root:
        d[b_root] = a_root


v,e = map(int,read().split())

mat = []

for _ in range(e):
    start,end,value = map(int,read().split())
    mat.append((start,end,value))

mat.sort(key=lambda x:x[2])

d = [i for i in range(v+1)]
result = 0
check = 0
for s,e,value in mat:

    if find(s)!=find(e):
        union(s,e)
        result+=value
        check+=1
    if check == v-1:
        print(result)
        break


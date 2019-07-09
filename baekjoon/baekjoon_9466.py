import sys
sys.setrecursionlimit(1111111)

def dfs(current) :
    global result
    global member
    global visited

    if visited[current]:
        if current in member:
            result += member.index(current)
        else :
            result += len(member)
        return

    visited[current] = 1
    member.append(current)
    dfs(mat[current])

t = int(input())

for _ in range(t):
    num = int(input())
    mat = [0]*(num+1)
    visited = [0]*(num+1)
    spl = list(map(int,input().split()))
    result = 0
    for i in range(len(spl)):
        mat[i+1] = spl[i]
    for i in range(len(mat)):
        if i==0:
            continue
        if visited[i]==1 :
            continue
        else :
            member = []
            dfs(i)
    print(result)
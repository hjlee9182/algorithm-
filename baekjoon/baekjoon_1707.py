import sys
input = sys.stdin.readline

def bfs_binary(v, visited, color):
    q = [v]
    visited[v] = True
    color[v] = 1
    while q:
        now = q.pop(0)
        for nxt in adj_lst[now]:
            if not visited[nxt]:
                q.append(nxt)
                color[nxt] = 3 - color[now]
                visited[nxt] = True
            else:
                if color[now] == color[nxt]:
                    return False
    return True

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    adj_lst = [[] for _ in range(n + 1)]
    for j in range(m):
        a, b = map(int, input().split())
        adj_lst[a].append(b)
        adj_lst[b].append(a)
    visited = [False for _ in range(n + 1)]
    color = [0 for _ in range(n + 1)]
    flag = True
    for node in range(1, n + 1):
        if not visited[node]:
            if not bfs_binary(node, visited, color):
                flag = False
                break
    if not flag:
        print("NO")
    else:
        print("YES")
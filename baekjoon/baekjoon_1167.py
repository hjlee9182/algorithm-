from collections import defaultdict, deque

def bfs(i):
    global d

    visit = [-1] * (len(d) + 1)
    q = deque()
    q.append(i)
    visit[i] = 0
    result = [0, 0]

    while q:
        x = q.popleft()
        for k, v in d[x].items():
            if visit[k] == -1:
                visit[k] = visit[x] + v
                q.append(k)
                if result[0] < visit[k]:
                    result = visit[k], k

    return result


n = int(input())

d = defaultdict(dict)

for _ in range(n):
    li = list(map(int, input().split()))
    for i in range(1,len(li)-2, 2):
        d[li[0]][li[i]] = li[i+1]

result = bfs(1)
result = bfs(result[1])

print(result[0])

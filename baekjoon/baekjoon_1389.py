from collections import defaultdict
from collections import deque


def bfs(q):
    check = dict()
    while len(q) > 0:
        now, num = q.popleft()
        if now not in check.keys():
            check[now] = num
        if now in check.keys():
            if num < check[now]:
                check[now] = num
        now_d = d[now]

        for k in now_d.keys():
            if k not in check.keys():
                q.append((k, num + 1))
    return sum(list(check.values()))


n, m = map(int, input().split())

user = dict()

d = defaultdict(dict)

for _ in range(m):
    f, t = map(int, input().split())
    d[f][t] = 1
    d[t][f] = 1
    user[t] = 1
    user[f] = 1

min_ = 192381902380913
target = 39482043824
for k in user.keys():
    q = deque()
    q.append((k, 0))
    value = bfs(q)
    if value < min_:
        min_ = value
        target = k
    elif value == min_ and k < target:
        target = k

print(target)

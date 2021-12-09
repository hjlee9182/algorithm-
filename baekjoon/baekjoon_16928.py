### using bfs
from collections import deque

n, m = map(int, input().split())

ladder = {}
snake = {}
for _ in range(n):
    x,y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    x, y = map(int, input().split())
    snake[x] = y

dp = [1000 for i in range(102)]
dp[1] = 0
q = deque()
q.append(1)
for i in range(2, 7):
    dp[i] = 1
    q.append(i)

while len(q) > 0:
    now = q.popleft()

    for i in range(1,7):

        target = now + i
        if target > 100:
            break

        if target in ladder.keys():
            target = ladder[target]
        elif target in snake.keys():
            target = snake[target]

        if dp[now] + 1 < dp[target]:
            dp[target] = dp[now] + 1
            q.append(target)
print(dp[100])

from collections import defaultdict

t = int(input())

for _ in range(t):
    c = int(input())
    d = defaultdict(int)
    for __ in range(c):
        li = list(map(str, input().split()))
        d[li[1]] += 1
    answer = 1
    for k in d.keys():
        answer *= d[k] + 1

    print(answer-1)



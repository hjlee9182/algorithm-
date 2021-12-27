from heapq import heappop, heappush, heapify
import sys

input = sys.stdin.readline


def sync(arr):
    while arr and not visit[arr[0][1]]:
        heappop(arr)


T = int(input())

for _ in range(T):
    visit = [False] * 1000001
    min_ = []
    max_ = []
    k = int(input())
    for __ in range(k):
        a, num = map(str, input().split())
        num = int(num)

        if a == 'I':
            heappush(min_, (num , __))
            heappush(max_, (-num, __))
            visit[__] = True
        else:
            if num == 1:
                sync(max_)

                if max_:
                    visit[max_[0][1]] = False
                    heappop(max_)
            else:
                sync(min_)

                if min_:
                    visit[min_[0][1]] = False
                    heappop(min_)

    sync(max_)
    sync(min_)

    if max_ and min_:
        print(-max_[0][0], min_[0][0])
        continue

    print("EMPTY")

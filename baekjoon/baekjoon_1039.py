import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

def bfs():
    q = deque()
    q.append((str(target),num))

    while q:
        t,n  = q.popleft()
        for i in range(len(t)-1) :
            for j in range(i+1,len(t)):
                now = list(t)
                now[j],now[i] = now[i],now[j]

                new = ''.join(now)
                if new[0] == '0':
                    continue
                if new not in visit[n-1]:
                    visit[n - 1].add(new)
                    if n > 0:
                        q.append((new,n-1))
    if len(visit[0])==0:
        print(-1)
        return
    print(max(visit[0]))
    return


target,num = map(int,read().split())
visit = [set() for i in range(11)]
#if(len(str(target))<2):print(-1)
bfs()
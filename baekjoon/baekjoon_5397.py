import collections

n = int(input())

for _ in range(n):
    first = collections.deque()
    last = collections.deque()
    l = input()
    for i in l:
        if i=='<':
            if len(first)>0:
                a = first.pop()
                last.appendleft(a)
        elif i=='>':
            if len(last)>0:
                a = last.popleft()
                first.append(a)
        elif i=='-':
            if len(first)>0:
                first.pop()
        else:
            first.append(i)
    st = ''
    for i in first:
        st+=i
    for i in last:
        st+=i
    print(st)
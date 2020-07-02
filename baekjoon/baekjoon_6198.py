import sys

read = lambda :sys.stdin.readline().strip()

n = int(read())
mat = []
for _ in range(n):
    mat.append(int(read()))


stack = []
answer = 0
for i in mat:

    if len(stack)==0:
        stack.append(i)
    else:
        while len(stack)>0 and i>=stack[-1]:
            stack.pop(-1)
        stack.append(i)

    answer+=len(stack)-1
print(answer)
n = int(input())
m = int(input())
s = input()

answer = 0
pattern = 0
i = 1

while i < m-1:
    if s[i-1] == 'I' and s[i] == 'O' and s[i+1] == 'I':
        pattern += 1
        if pattern == n:
            pattern -= 1
            answer += 1
        i += 1
    else:
        pattern = 0
    i += 1

print(answer)


mat = [0 for i in range(26)]


l = input()
for i in l:
    a = ord(i)-97
    mat[a]+=1
st = ''
for i in range(26):
    mat[i] = str(mat[i])
print(' '.join(mat))
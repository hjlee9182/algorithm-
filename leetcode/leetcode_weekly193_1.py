

def hi(a):
    mat = []

    for i in range(1,len(a)+1):
        mat.append(sum(a[:i]))
    return mat

print(hi([1,2,3,4]))
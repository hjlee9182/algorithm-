

def hi(nums,n):
    a = nums[:n]
    b = nums[n:]
    mat = []
    for i in range(n):
        mat.append(a[i])
        mat.append(b[i])
    return mat


print(hi([1,2,3,4]))
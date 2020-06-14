import collections

def hi(arr,k):

    a = collections.defaultdict(int)
    for i in arr:
        a[i] +=1

    d = sorted(a.items(), key=lambda x:x[1])
    for i in range(len(d)):
        if k>=d[i][1]:
            k-=d[i][1]
            if k==0:
                return len(d)-i-1
        else:
            return len(d)-i




print(hi([5,5,4],1))
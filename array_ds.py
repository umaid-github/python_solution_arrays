def reverseArray(a):
    n=len(a)
    s,e=0,n-1
    while s<e:
        a[s],a[e]=a[e],a[s]
        s=s+1
        e=e-1
    return a
if __name__=='__main__':
    n=int(input())
    a=list(map(int,input().split()))
    res=reverseArray(a)
    for i in res:
        print(i,end=" ")
    print()

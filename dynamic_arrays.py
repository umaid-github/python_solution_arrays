def dynamicArrays(n,queries):
    lastAnswer=0
    l=[]
    seqList=[[] for _ in range(n)]
    for i in queries:
        index=(i[1]^lastAnswer)%n
        if i[0]==1:
            seqList[index].append(i[2])
        elif i[0]==2:
            lastAnswer=seqList[index][i[2]%len(seqList[index])]
            l.append(lastAnswer)
    return l

if __name__=='__main__':
    n,q=map(int,input().split())
    queries=[]
    for _ in range(q):
        queries.append(list(map(int,input().split())))
    res=dynamicArrays(n,queries)
    for i in res:
        print(i,end=" ")

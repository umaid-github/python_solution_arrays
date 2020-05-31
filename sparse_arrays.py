def matchingStrings(strings,queries):
    l=list()
    for name in queries:
        l.append(strings.count(name))
    return l

if __name__=='__main__':
    n=int(input())
    strings=[]
    for _ in range(n):
        strings.append(input())
    m=int(input())
    queries=[]
    for _ in range(m):
        queries.append(input())
    res=matchingStrings(strings,queries)
    for i in res:
        print(i,end=' ')

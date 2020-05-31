def addition(n):
    return n+n
num=[1,2,3,4]
mapped=set(map(addition,num))
for i,j in zip(mapped):
    print(i)

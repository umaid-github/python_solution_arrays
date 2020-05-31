def hourglasssum(arr):
    m=-63
    sum=0
    for i in range(4):
        for j in range(4):
            sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            m=max(m,sum)
            sum=0
    return m

def hourglassSum(arr):
    m=-63
    hourglass=0
    for i in range(4):
        for j in range(4):
            top=sum(arr[i][j:j+3])
            mid=arr[i+1][j+1]
            bottom=sum(arr[i+2][j:j+3])
            hourglass=top+mid+bottom
            m=max(m,hourglass)
            hourglass=0
    return m

if __name__=='__main__':
    arr=[]
    for _ in range(6):
        arr.append(list(map(int,input().split())))
    print(hourglassSum(arr))

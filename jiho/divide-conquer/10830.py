#행렬 제곱
import sys
input=sys.stdin.readline

n,b=map(int,input().split())

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        arr[i][j]%=1000

def mat_multi(a,b):

    global n
    rt=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                rt[i][j]+=a[i][k]*b[k][j]
            rt[i][j]%=1000
    
    return rt

def solve(b):
    if b==1:
        return arr
    elif b==2:
        return mat_multi(arr,arr)
    else:
        temp=solve(b//2)
        if b%2==0:
            return mat_multi(temp,temp)
        else:
            return mat_multi(mat_multi(temp,temp),arr)

result=solve(b)
for elem in result:
    for i in elem:
        print(i,end=" ")
    print()



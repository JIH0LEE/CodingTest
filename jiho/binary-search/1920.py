#수 찾기
import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
m=int(input())
inputs=list(map(int,input().split()))
result=[0 for i in range(m)]
for i in range(m):
    elem=inputs[i]
    left=0
    right=n-1
    while left<=right:
        mid=(left+right)//2
        target=arr[mid]
        if elem==target:
            result[i]=1
            break
        elif elem>target:
            left=mid+1
        else:
            right=mid-1

for elem in result:
    print(elem)
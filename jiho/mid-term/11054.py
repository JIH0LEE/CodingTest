#가장 긴 바이토닉 부분 수열
import sys
input=sys.stdin.readline
n=int(input())
inputs=list(map(int,input().split()))
dp1=[0 for _ in range(n)] #앞에서 부터 증가하는 부분 수열
dp2=[0 for _ in range(n)] #뒤에서 부터 증가하는 부분 수열 
result=[]
for i in range(n):
    for j in range(i):
        if dp1[i]<dp1[j] and inputs[i]>inputs[j]:
            dp1[i]=dp1[j]
        
    dp1[i]+=1

for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if dp2[i]<dp2[j] and inputs[i]>inputs[j]:
            dp2[i]=dp2[j]
    
    dp2[i]+=1

for i in range(n):
    result.append(dp1[i]+dp2[i]-1)

print(max(result))
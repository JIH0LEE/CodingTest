#N-Queen
#파이썬으로 하면 왜 시간초과일까    
import sys
input=sys.stdin.readline

n=int(input())
cnt=0
ans=0
result=[]
def check(num):
    if num in result:
        return False
    length=len(result)
    for i in range(length):
        p=length-i
        if (num==result[i]+p) or (num==result[i]-p):
            return False
    
    return True

def solve(cnt):
    global ans
    if cnt==n:
        ans+=1
        return

    for i in range(0,n):
        t=check(i)
        if t:
            result.append(i)
            solve(cnt+1)
            result.pop()
        else:
            continue
solve(0)
print(ans)


#조합 0의 개수
#메모리 초과?
#시간 초과?
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
def find_count(n,m,k):
    count=0
    for i in range(m+1,n+1):
        num=i
        while True:
            if num%k !=0:
                break
            count+=1
            num=num//k

    return count
five_count=find_count(n,n-m,5)-find_count(m,1,5)
two_count=find_count(n,n-m,2)-find_count(m,1,2)

print(min(five_count,two_count))
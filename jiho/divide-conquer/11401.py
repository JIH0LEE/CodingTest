#이항계수 3
#메모리 초과
#몰라
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n,k=map(int,input().split())
def solve(n,r):
    if n==1 or r==0 or n==r:
        return 1
    
    return (solve(n-1,r)+solve(n-1,r-1))%1000000007

print(solve(n,k))
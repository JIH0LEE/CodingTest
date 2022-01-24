#이항계수 1
#nCr=n-1Cr+n-1Cr-1
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n,k=map(int,input().split())
comb=[[None for i in range(j+1)] for j in range(n+1)]

for i in range(n+1):
    comb[i][0]=1
    comb[i][i]=1
    


def solve(n,r):
    if not comb[n][r]:
        comb[n][r]=solve(n-1,r-1)+solve(n-1,r)

    return comb[n][r]
print(solve(n,k))

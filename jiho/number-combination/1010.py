#다리 놓기
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

t=int(input())

comb=[[None for i in range(j+1)] for j in range(31)]
def solve(n,r):
    if not comb[n][r]:
        comb[n][r]=solve(n-1,r-1)+solve(n-1,r)

    return comb[n][r]
for i in range(31):
    comb[i][0]=1
    comb[i][i]=1

for i in range(t):
    n,m=map(int,input().split())
    print(solve(m,n))
#내리막 길
import sys
input=sys.stdin.readline
m,n=map(int,input().split())
mat=[]
for _ in range(m):
    mat.append(list(map(int,input().split())))

#현재 위치에서 목표까지 갈 수 방법의 수(-1은 not visited)
dp=[[-1 for i in range(n)] for j in range(m)]

def solve(x,y):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    if x==0 and y==0:
        dp[0][0]=1
    elif dp[x][y]==-1:
        dp[x][y]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and mat[x][y]<mat[nx][ny]:
                dp[x][y]+=solve(nx,ny)
            
    
    return dp[x][y]

print(solve(m-1,n-1))
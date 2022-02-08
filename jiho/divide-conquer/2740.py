#행렬 곱셈
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
m,k=map(int,input().split())
b=[]
for i in range(m):
    b.append(list(map(int,input().split())))
result=[[0 for i in range(k)] for j in range(n)]


for i in range(n):
    for j in range(k):
        for l in range(m):
            result[i][j]+=a[i][l]*b[l][j]

for elems in result:
    for elem in elems:
        print(elem,end=" ")
    print()
#패션왕 신해빈
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline


t=int(input())
for i in range(t):
    n=int(input())
    dic=dict()
    result=1
    for j in range(n):
        elem=input().split()
        if elem[1] in dic:
            dic[elem[1]]+=1
        else:
            dic[elem[1]]=1
    for val in dic.values():
        result*=(val+1)
    result-=1

    print(result)
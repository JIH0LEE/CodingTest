#회의실 배정
import sys
input=sys.stdin.readline
n=int(input())
inputs=[]
for i in range(n):
    start,end=map(int,input().split())
    inputs.append((start,end))

inputs.sort(key=lambda x:x[0])
inputs.sort(key=lambda x:x[1])

result=[inputs[0]]
for elem in inputs[1:]:
    if elem[0]>=result[-1][1]:
        result.append(elem)

print(len(result))


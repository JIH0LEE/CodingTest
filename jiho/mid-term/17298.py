#오큰수
import sys
input=sys.stdin.readline
n=int(input())
inputs=list(map(int,input().split()))
stack=[0]    #아직 오큰수가 정해지지 않은 값들이 들어가 있음, 인덱스의 값이 들어감
result=[-1 for i in range(n)]
for i in range(1,n):
    while True:
        if not stack:   #스택이 비어있을 때
            stack.append(i)
            break
        if inputs[stack[-1]]<inputs[i]:
            elem=stack.pop()
            result[elem]=inputs[i]
            continue
        else:
            stack.append(i)
            break
for elem in result:
    print(elem,end=" ")



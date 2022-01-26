#스택
import sys
input=sys.stdin.readline
n=int(input())
stack=[]
for i in range(n):
    line=input().split()
    com=line[0]
    if com=='push':
        stack.append(line[1])
    elif com=='pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
        
    elif com=='size':
        print(len(stack))
    elif com=='empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
    


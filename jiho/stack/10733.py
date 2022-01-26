#제로
import sys
input=sys.stdin.readline
stack=[]
n=int(input())
for i in range(n):
    a=int(input())
    if a==0:
        stack.pop()
    else:
        stack.append(a)

print(sum(stack))
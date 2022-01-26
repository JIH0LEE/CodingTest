#괄호
import sys
input=sys.stdin.readline
n=int(input())
for i in range(n):
    line=input().strip()
    stack=[]
    flag=True
    for j in range(len(line)):
        if line[j]=='(':
            stack.append('(')
        else:
            if not stack:
                flag=False
                break
            else:
                if stack[-1]!='(':
                    flag=False
                    break
                else:
                    stack.pop()
    if not stack and flag:
        print('YES')
    else:
        print('NO')

    if not stack and flag:
        print('YES')
    else:
        print('NO')
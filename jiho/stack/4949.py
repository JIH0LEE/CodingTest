#균형잡힌 세상
while True:
    line=input()
    if line=='.':
        break
    stack=[]
    flag=True
    for elem in line[:-1]:
        if elem=='(' or elem=='[':
            stack.append(elem)
        elif elem==')':
            if not stack:
                flag=False
                break
            else:
                if stack[-1]!='(':
                    flag=False
                    break
                else:
                    stack.pop()
        elif elem==']':
            if not stack:
                flag=False
                break
            else:
                if stack[-1]!='[':
                    flag=False
                    break
                else:
                    stack.pop()
    if not stack and flag:
        
        print('YES')
    else:
        print('NO')

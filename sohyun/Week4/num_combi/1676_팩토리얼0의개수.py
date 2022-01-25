def fact(n):
    if n>=2:
        return n*fact(n-1)
    else:
        return 1

n = int(input())
cnt = 0
for i in str(fact(n))[::-1]:
    if i == '0':
        cnt += 1
    else:
        break

print(cnt)

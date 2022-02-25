n = int(input())
s = list(map(int, input().split()))
res = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if s[i] > s[j] and res[i] < res[j]:
            res[i] = res[j]
    res[i] = res[i] + 1

print(max(res))
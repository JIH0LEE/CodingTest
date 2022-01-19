n = int(input())
s = list(map(int, input().split()))
dp1 = [0 for i in range(n)]
dp2 = [0 for i in range(n)]
res = []


for i in range(n):
    for j in range(i):
        if s[i] > s[j] and dp1[i] < dp1[j]:
            dp1[i] = dp1[j]
    dp1[i] += 1

print(dp1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i-1, -1):
        if s[i] > s[j] and dp2[i] < dp2[j]:
            dp2[i] = dp2[j]
    dp2[i] += 1

print(dp2)

for i in range(n):
    res.append(dp1[i] + dp2[i])

print(max(res)-1)
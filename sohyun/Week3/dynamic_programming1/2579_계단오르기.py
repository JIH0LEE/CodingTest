n = int(input())
s = [0 for i in range(301)]
res = [0 for i in range(301)]

for i in range(n):
    s[i] = int(input())
res[0] = s[0]
res[1] = s[0] + s[1]
res[2] = max(s[1] + s[2], s[0] + s[2])
for i in range(3, n):
    res[i] = max(res[i - 3] + s[i - 1] + s[i], res[i - 2] + s[i])
print(res[n - 1])
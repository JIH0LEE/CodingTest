n = int(input())
s = [0]
res = [0]
for i in range(n):
    s.append(int(input()))
res.append(s[1])

if n > 1:
    res.append(s[1] + s[2])

for i in range(3, n + 1):
    res.append(max(res[i - 1], res[i - 3] + s[i - 1] + s[i], res[i - 2] + s[i]))

print(res[n])
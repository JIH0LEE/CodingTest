import math

n = int(input())
s = []
diff = []
res = set()
for _ in range(n):
    s.append(int(input()))

for i in range(0, n-1):
    diff.append(s[i+1] - s[i])

if n > 2:
    g_cd = math.gcd(diff[0], diff[1])
else:
    g_cd = diff[0]

for i in range(2, n-1):
    g_cd = math.gcd(diff[i], g_cd)

for i in range(1, int(round(g_cd**0.5))+1):
    if g_cd % i == 0:
        res.add(i)
        res.add(g_cd//i)

res = sorted(list(res))
for i in res[1:]:
    print(i, end = ' ')

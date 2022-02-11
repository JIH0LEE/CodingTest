n = int(input())
s = []

for i in range(n):
    a, n = map(str, input().split())
    s.append((int(a), n))

s.sort(key = lambda x:(x[0]))

for x in s:
    print(x[0], x[1])
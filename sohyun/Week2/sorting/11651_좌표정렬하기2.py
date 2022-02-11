n = int(input())
s = []

for i in range(n):
    x, y = map(int, input().split())
    s.append((x, y))

s.sort(key = lambda i:(i[1], i[0]))


for i in s:
    print(i[0], i[1])
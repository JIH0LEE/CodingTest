n = int(input())
we_he = []
rank = []

for i in range(n):
    w, h = map(int, input().split())
    we_he.append((w, h))

for i in range(n):
    cnt = 0
    for j in range(n):
        if we_he[i][0] < we_he[j][0] and we_he[i][1] < we_he[j][1]:
            cnt += 1
    rank.append(cnt + 1)

for i in rank:
    print(i, end=" ")
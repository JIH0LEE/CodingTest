n,m = map(int, input().split())
cards = list(map(int, input().split()))

res = 0
length = len(cards)

for i in range (0, length):
    for j in range(i+1, length):
        for k in range (j+1, length):
            temp = cards[i] + cards[j] + cards[k]
            if temp <= m:
                res = max(res, temp)
print(res)
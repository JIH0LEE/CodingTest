n = int(input())
li = list(map(int, input().split()))
res = [-1 for _ in range(n)]

prev_pop = 0
curr_pop = 0

for i in range(n-1,0,-1):
    prev_pop = li.pop()
    curr_pop = li[i-1]
    if prev_pop > curr_pop:
        res[i-1] = prev_pop
    else:
        if curr_pop > res[i]:
            continue
        else:
            res[i-1] = res[i]

print(res)










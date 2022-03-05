n = int(input())
li = list(map(int, input().split()))
res = [-1 for _ in range(n)]

prev_pop = 0
curr_pop = 0

for i in range(n-1,0,-1):
    prev_pop = li.pop()
    curr_pop = li[i-1]
    if prev_pop > curr_pop: #가장 오른쪽것을 검색
        res[i-1] = prev_pop
    else:
        for elem in res[i:]:
            if curr_pop>elem:
                continue
            else:
                res[i-1]=elem
                break
        

for elem in res:
    print(elem,end=" ")
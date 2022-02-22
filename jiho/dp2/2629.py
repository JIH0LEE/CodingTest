# 양팔 저울
import sys
input = sys.stdin.readline
n = int(input())
choo = list(map(int, input().split()))
m = int(input())
bead = list(map(int, input().split()))
choo_sum = sum(choo)
dp = [[False for i in range(choo_sum+1)] for j in range(n)]
dp[0][choo[0]] = True
dp[0][choo_sum-choo[0]] = True
dp[0][choo_sum-choo[0]*2] = True
dp[0][choo_sum] = True
for i in range(1, n):
    temp = set()
    weight = choo[i]
    for j in range(0, choo_sum+1):
        if dp[i-1][j]:
            dp[i][j] = True
            temp1 = [choo[i], j-choo[i], j-2*choo[i]]
            for elem in temp1:
                if 0 <= elem:
                    temp.add(elem)
    for elem in temp:
        dp[i][elem] = True

for elem in bead:
    if elem > choo_sum:
        print("N", end=" ")
    elif dp[n-1][elem]:
        print("Y", end=" ")
    else:
        print("N", end=" ")

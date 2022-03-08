# 파일합치기
# pypy3통과
# python3 시간초과 ㅠㅠ
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [[]]
    input_files = list(map(int, input().split()))
    sum = [0]
    for elem in input_files:
        sum.append(sum[-1]+elem)
    temp = [0]*(n+1)
    dp.append(temp)
    for i in range(2, n+1):
        new_dp = [0]
        for j in range(1, n-i+2):
            mid_sum = sum[i+j-1]-sum[j-1]
            temp = [dp[k][j]+dp[i-k][k+j]+mid_sum for k in range(1, i)]
            min_num = min(temp)
            new_dp.append(min_num)
        dp.append(new_dp)
    print(dp[n][1])

# 두 수의 합
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
start = 0
end = n-1
arr.sort()
count = 0
while start < end:
    if arr[start]+arr[end] == x:
        count += 1
        start += 1
        end -= 1

    elif arr[start]+arr[end] < x:
        start += 1

    else:
        end -= 1
print(count)

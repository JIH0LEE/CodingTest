# 두 용액
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
start = 0
end = n-1
a = 0
b = 0
min = 2000000001

while start < end:
    sum = arr[start]+arr[end]
    if sum == 0:
        a = start
        b = end
        break
    if sum < 0:
        if abs(sum) < min:
            min = abs(sum)
            a = start
            b = end
        start += 1
    else:
        if abs(sum) < min:
            min = abs(sum)
            a = start
            b = end
        end -= 1
print(arr[a], arr[b])

# 통계학
import sys
input = sys.stdin.readline

n = int(input())
counts = [0]*8001
inputs = []
for i in range(n):
    num = int(input())
    inputs.append(num)
    counts[num+4000] += 1

inputs.sort()


def find_mode(arr):
    is_second = False
    rt = 0
    count = 0
    for idx, value in enumerate(arr):
        if value == 0:
            continue
        if value == count:
            if not is_second:
                is_second = True
                count = value
                rt = idx-4000

        elif value > count:
            is_second = False
            count = value
            rt = idx-4000

        else:
            continue

    return rt


mean = round(sum(inputs)/n)
center = inputs[n//2]
mode = find_mode(counts)
range = inputs[-1]-inputs[0]


print(mean)
print(center)
print(mode)
print(range)

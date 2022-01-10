# 좌표 압축

import sys
input = sys.stdin.readline

n = int(input())
inputs = list(map(int, input().split()))


s = set(inputs)
dictionary = {num: 0 for num in s}

sorted_list = sorted(s)

for i in range(len(sorted_list)):
    elem = sorted_list[i]
    dictionary[elem] = i

for elem in inputs:
    print(dictionary[elem], end=" ")

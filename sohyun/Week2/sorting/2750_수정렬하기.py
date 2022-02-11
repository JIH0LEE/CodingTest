# 버블정렬
import sys

def bubble_sort(s):
    for i in range(len(s)):
        for j in range(0, len(s)-i-1):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
    return s

n = int(input())
li = []
for _ in range(n):
    num = int(sys.stdin.readline())
    li.append(num)
    
for i in bubble_sort(li):
    print(i)
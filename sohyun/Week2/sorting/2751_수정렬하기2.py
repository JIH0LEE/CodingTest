import sys

n = int(input())
s = []
for i in range(n):
    num = int(sys.stdin.readline())
    s.append(num)

for i in sorted(s):
    print(i)
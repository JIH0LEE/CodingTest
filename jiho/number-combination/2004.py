# 조합 0의 개수
# 메모리 초과?
# 시간 초과?
import sys
input = sys.stdin.readline

n, m = map(int, input().split())


def find_count(n):
    count2 = 0
    count5 = 0
    num2 = 2
    num5 = 5
    while num2 <= n:
        count2 += (n//num2)
        num2 = 2*num2
    while num5 <= n:
        count5 += (n//num5)
        num5 = 5*num5

    return (count2, count5)


a = find_count(n)
b = find_count(n-m)
c = find_count(m)

print(min(a[0]-b[0]-c[0], a[1]-b[1]-c[1]))

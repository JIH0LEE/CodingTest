n, m = map(int, input().split())

def cnt_two(n):
    x = 1
    sum = 0
    while pow(2, x) <= n:
        sum += n//pow(2, x)
        x += 1
    return sum

def cnt_five(n):
    x = 1
    sum = 0
    while pow(5, x) <= n:
        sum += n//pow(5, x)
        x += 1
    return sum


print(min(cnt_two(n) - cnt_two(m) - cnt_two(n-m), cnt_five(n) - cnt_five(m) - cnt_five(n-m)))
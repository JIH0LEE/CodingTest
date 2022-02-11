n, m = list(map(int, input().split()))
s = []

def n_and_m(x):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(x, n+1):
        s.append(i)
        n_and_m(i)
        s.pop()

n_and_m(1)
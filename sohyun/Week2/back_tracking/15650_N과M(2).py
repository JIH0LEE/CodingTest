n, m = list(map(int, input().split()))
s = []

def n_and_m(x):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(x, n+1):
        if i not in s:
            s.append(i)
            n_and_m(i+1)
            s.pop()

n_and_m(1)
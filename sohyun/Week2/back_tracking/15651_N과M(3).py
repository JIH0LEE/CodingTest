n, m = list(map(int, input().split()))
s = []

def n_and_m():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        s.append(i)
        n_and_m()
        s.pop()

n_and_m()
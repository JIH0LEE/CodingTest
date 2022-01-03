# 하노이 탑 이동 순서

# src,middle,dest
# n-1개를 middle로 옮김
# 마지막 1개를 dest로 옮김
# middle에 있는 n-1개를 dest로 옮김


def solve(n, src, middle, dest):
    global result
    global count

    if n == 1:
        count += 1
        result.append((src, dest))
    else:
        solve(n-1, src, dest, middle)
        solve(1, src, middle, dest)
        solve(n-1, middle, src, dest)


result = []
count = 0
n = int(input())
solve(n, 1, 2, 3)
print(count)
for elem in result:
    print(elem[0], elem[1])

from sys import stdin
n = stdin.readline()
n_int = map(int,stdin.readline().split())
m = stdin.readline()
m_int = map(int,stdin.readline().split())
n_int = sorted(n_int)

def binary_search(i, n_int, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if i == n_int[mid]:
        return n_int[start:end+1].count(i)
    elif i < n_int[mid]:
        return binary_search(i, n_int, start, mid-1)
    else:
        return binary_search(i, n_int, mid+1, end)


dic = {}
for i in n_int:
    start = 0
    end = len(n_int)-1
    if i not in dic:
        dic[i] = binary_search(i, n_int, start, end)

print(' '.join(str(dic[j]) if j in dic else '0' for j in m_int))


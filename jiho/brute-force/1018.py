# 체스판 다시 칠하기

def check(data):
    global answer_data
    rt = 2500
    for i in range(2):
        min = 0
        for j in range(8):
            for k in range(8):
                if data[j][k] != answer_data[i][j][k]:
                    min += 1
        if min < rt:
            rt = min

    return rt


n, m = map(int, input().split())
arr = []
min = 2500
check_data = ['BWBWBWBW', 'WBWBWBWB']
answer_data = [[], []]


for j in range(8):
    answer_data[0].append(check_data[j % 2])
    answer_data[1].append(check_data[1-j % 2])

for i in range(n):
    arr.append(input())

for i in range(0, n+1-8):
    for j in range(0, m+1-8):
        temp = []
        for k in range(i, i+8):
            temp.append(arr[k][j:j+8])
        rt = check(temp)
        if rt < min:
            min = rt

print(min)

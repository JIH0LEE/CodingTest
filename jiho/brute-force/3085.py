# 사탕 게임

# 오른쪽과 아래로만 교환하면 된다(중복x)

# 바꾼다음에 check

import sys
import copy

input = sys.stdin.readline

n = int(input())

graph = []
result = 0
dy = [0, 1]
dx = [1, 0]

for i in range(n):
    graph.append(list(input()[0:n]))

for i in range(n):
    for j in range(n):
        elem = graph[i][j]
        for k in range(2):
            ny = i+dy[k]
            nx = j+dx[k]
            if ny < n and nx < n:
                swap_elem = graph[ny][nx]
                if elem != swap_elem:
                    temp_graph = copy.deepcopy(graph)
                    temp_graph[ny][nx] = elem
                    temp_graph[i][j] = swap_elem

                    count = 1
                    max = 0

                    for k in range(n):
                        fst = temp_graph[0][k]
                        count = 1
                        for l in range(1, n):
                            cmp = temp_graph[l][k]
                            if fst == cmp:
                                count += 1
                                if count > max:
                                    max = count
                            else:
                                if count > max:
                                    max = count
                                count = 1
                            fst = cmp
                    if result < max:
                        result = max

                    count = 1
                    max = 0
                    for k in range(n):
                        count = 1
                        fst = temp_graph[k][0]
                        for l in range(1, n):
                            cmp = temp_graph[k][l]
                            if fst == cmp:
                                count += 1
                                if count > max:
                                    max = count
                            else:
                                if count > max:
                                    max = count
                                count = 1
                            fst = cmp
                    if result < max:
                        result = max


print(result)

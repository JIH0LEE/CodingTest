import sys
sys.setrecursionlimit(1000000)

def dfs(n,boolVal):
    state[n-1] = (True,boolVal)
    for i in graph[n-1]:
        if not state[i-1][0] :
            dfs(i,1-boolVal)
        else:
            if state[i-1][1] != boolVal:
                continue
            else:
                boolArr.append(0)

T = int(input())
answer = []
for _ in range(T):
    vNum, eNum = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(vNum)]
    state = [(False,0)]*vNum
    boolArr = []
    for _ in range(eNum):
        a, b = map(int, sys.stdin.readline().split())
        graph[a-1].append(b)
        graph[b-1].append(a)
    for i in range(vNum):
        if state[i][0] == False:
            dfs(i+1,0)
    if len(boolArr) == 0:
        answer.append("YES")
    else:
        answer.append("NO")

for i in range(len(answer)):
    print(answer[i])
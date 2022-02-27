def dfs(x, y): 
    if x <= -1 or y <= -1 or x >= N or y >= N :
        return 
    if graph[x][y] == 0:
        return
    elif graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return
        
N = int(input())
graph = [[]*N for _ in range(N)]
countList = []
for i in range(N):
    graph[i] = list(map(int,input()))
count = 0

for i in range(N):
    for j in range(N):
        dfs(i,j)
        if count != 0:
            countList.append(count)
        count = 0

countList.sort()
print(len(countList))
for i in range(len(countList)):
    print(countList[i])
from collections import deque

num = int(input())
deq = deque([i for i in range(1, num + 1)])

while len(deq) != 1:
    deq.popleft()
    deq.append(deq.popleft())

print(deq[0])
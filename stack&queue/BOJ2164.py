from collections import deque

n = int(input())
deque = deque()

for i in range(1, n + 1):
    deque.append(i)

while len(deque) > 1:
    deque.popleft()
    deque.rotate(-1)

print(deque[0])

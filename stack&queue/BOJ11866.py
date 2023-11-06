from collections import deque

n, k = map(int, input().split())
deque = deque()
result = []
for i in range(1, n + 1):
    deque.append(i)

for _ in range(n):
    deque.rotate(-(k - 1))
    result.append(deque.popleft())

print("<", end="")
for data in result:
    print(data, end="")
    if data != result[len(result) - 1]:
        print(", ", end="")
print(">", end="")

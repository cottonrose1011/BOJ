from collections import deque

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
m = int(input())
C = list(map(int, input().split()))
queueStack = deque()
result = []

for idx, value in enumerate(B):
    if A[idx] == 0:
        queueStack.append(value)

for i in C:
    queueStack.appendleft(i)

for _ in range(m):
    result.append(queueStack.pop())
print(*result)

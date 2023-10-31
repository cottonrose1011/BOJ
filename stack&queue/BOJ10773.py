import sys
input = sys.stdin.readline

k = int(input())
stack = []
for _ in range(k):
    n = int(input())
    stack.append(n) if n != 0 else stack.pop()
print(sum(stack))

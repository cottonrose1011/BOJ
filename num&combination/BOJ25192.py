import sys

input = sys.stdin.readline

n = int(input())
chat = {}
result = 0

for _ in range(n):
    s = input()
    if s == 'ENTER':
        chat.clear()
    elif s in chat:
        continue
    else:
        chat[s] = 1
        result += 1
print(result)

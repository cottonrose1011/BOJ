from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
deque = deque()

for _ in range(n):
    command = input().split()

    if command[0] == '1':
        deque.appendleft(command[1])
    elif command[0] == '2':
        deque.append(command[1])
    elif command[0] == '3':
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif command[0] == '4':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif command[0] == '5':
        print(len(deque))
    elif command[0] == '6':
        print(1 if not deque else 0)
    elif command[0] == '7':
        print(deque[0] if deque else -1)
    elif command[0] == '8':
        print(deque[-1] if deque else -1)

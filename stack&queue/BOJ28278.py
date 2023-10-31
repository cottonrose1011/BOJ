import sys
input = sys.stdin.readline

n = int(input())
stack = []
command = []
for _ in range(n):
    command.append(input().split())
for i in range(len(command)):
    if command[i][0] == '1':
        stack.append(int(command[i][1]))
    elif command[i][0] == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[i][0] == '3':
        print(len(stack))
    elif command[i][0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

import sys
input = sys.stdin.readline

n = int(input())
emp = {}

for _ in range(n):
    name, state = input().split()
    emp[name] = state

for name, state in sorted(emp.items(), reverse=True):
    if state == 'enter':
        print(name)

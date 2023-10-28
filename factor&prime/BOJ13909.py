import sys
input = sys.stdin.readline

n = int(input())
i = 1
result = 0
while i*i <= n:
    i += 1
    result += 1
print(result)

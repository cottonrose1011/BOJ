import sys
input = sys.stdin.readline

n = int(input())
array = []
dp2 = [1] * n
for _ in range(n):
    a, b = map(int, input().split())
    array.append((a, b))
array.sort()
for i in range(n):
    for j in range(i):
        if array[j][1] < array[i][1]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

print(n-max(dp2))

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
dp = [0] * n
dp[0] = array[0]

for i in range(1, n):
    dp[i] = dp[i-1] + array[i]

for _ in range(m):
    a, b = map(int, input().split())
    if a == b:
        print(array[a-1])
    elif a == 1:
        print(dp[b-1])
    else:
        print(dp[b-1] - dp[a-2])

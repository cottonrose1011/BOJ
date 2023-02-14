import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = [[0, 0]]
for _ in range(n):
    w, v = map(int, input().split())
    array.append([w, v])

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = array[i][0]
        value = array[i][1]
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            before = dp[i-1][j]
            after = value + dp[i-1][j-weight]
            dp[i][j] = max(before, after)

print(dp[n][k])

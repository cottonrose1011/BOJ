n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*i for i in range(1, n+1)]
dp[0] = array[0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + array[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + array[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1] + array[i][j], dp[i-1][j] + array[i][j])
print(max(dp[-1]))

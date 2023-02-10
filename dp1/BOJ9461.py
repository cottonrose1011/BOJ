t = int(input())
dp = [1] * 101
for _ in range(t):
    n = int(input())
    dp[4] = 2
    dp[5] = 2
    dp[6] = 3
    for i in range(7, 101):
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[n])

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
dp = [[] for _ in range(n)]
dp[0] = array[0]

for i in range(1, n):
    dp[i] = [array[i][0] + min(dp[i-1][1], dp[i-1][2]),
             array[i][1] + min(dp[i-1][0], dp[i-1][2]),
             array[i][2] + min(dp[i-1][0], dp[i-1][1])
             ]
print(min(dp[n-1]))

n = int(input())
INF = -float("inf")
dp = [INF] * 100002
array = list(map(int, input().split()))
dp[0] = array[0]

for i in range(1, n):
    if dp[i-1] > 0:
        dp[i] = dp[i-1] + array[i]
    else:
        dp[i] = array[i]

print(max(dp))

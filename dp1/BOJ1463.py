n = int(input())

dp = [0] * 1000001

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    # 1을 빼준 것과 3이나 2로 나눴을 때의 횟수를 비교하여 dp 채워나감.

print(dp[n])

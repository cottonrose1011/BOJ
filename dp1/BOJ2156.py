n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
dp = [0] * 10001
dp[1] = array[0]
if n > 1:
    dp[2] = array[1] + dp[1]
for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + array[i-1], dp[i-3] + array[i-1] + array[i-2])
print(dp[n])

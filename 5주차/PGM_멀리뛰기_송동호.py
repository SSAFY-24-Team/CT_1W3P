dp = [0]*10000

dp[1] = 1
dp[2] = 2

for i in range(3,2001):
    dp[i] = dp[i-1] + dp[i-2]

print()


a = 5

dp = [0]*10

dp[0] = 0
dp[1] = 1

for i in range(1,a):
    dp[i+1] = dp[i] + dp[i-1]

print(dp)


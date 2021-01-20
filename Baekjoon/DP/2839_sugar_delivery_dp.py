# dp 방식
n = int(input())
dp = [9999] * 5001
dp[3] = dp[5] = 1
# 5부터 이제 하나씩 증가해나가야 하기 때문
# tabulation
for i in range(6, n + 1):
    dp[i] = min(dp[i - 3], dp[i - 5]) + 1
if dp[n] >= 9999:
    print(-1)
else:
    print(dp[n])
n = int(input())
dp = [0 for i in range(1000001)]
def solution(n):
    global dp
    i = 2
    while i <= n:
        dp[i] = dp[i-1] + 1
        if i % 2 == 0:
            # dp[i]일 경우에는 이전껏을 + 1 한 상태이고
            # dp[i//2]의 경우에는 이전것이 아닌 i//2 일때를 더하는 것
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
        i += 1

solution(n)
result = dp[n]
print(result)


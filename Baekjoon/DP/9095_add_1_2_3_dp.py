### backtracking으로도 풀 수 있음
# 백트래킹은 dp로도 풀 수 있음
n = int(input())
# 상향식으로 나타내는 dp값을 구할 예정
def cal(now):
    # now까지 계속해서 더해서 구해나가는 형식
    dp = [0] * (now + 1)
    # 1의 합으로 구성되는 경우가 있기 때문에 처음원소를 1로 초기화
    dp[0] = 1
    for i in range(1, now + 1):
        if i - 1 >= 0:
            dp[i] += dp[i - 1]
        if i - 2 >= 0:
            dp[i] += dp[i - 2]
        if i - 3 >= 0:
            dp[i] += dp[i - 3]
    return dp[now]

for _ in range(n):
    num = int(input())
    ans = cal(num)
    print(ans)
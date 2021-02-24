# 시간에 따른 값을 입력하고 n + 1 일이 되었을때 얻을 수 있는 최대 값을 구하기
n = int(input())
t = []
data = [tuple(map(int, input().split())) for i in range(n)]
# n + 1 번째까지 고려해야 하기 때문
dp = [0] * (n + 1)
# index는 0부터 시작해서 n + 1까지 고려
# 만약 현재 index + data[i][0] 이 작다면 그 값을 dp[i + data[i][0]] 에 업데이트 가능
# 그 조건은 dp[i + data[i][0]] 에 dp[i] + data[i][1] 과 기존의 값 비교
# 그리고 dp[i + 1] 에다가 다시 값 넣기
for i in range(n):
    if data[i][0] + i <= n:
        dp[i + data[i][0]] = dp[i] + data[i][1] if dp[i] + data[i][1] > dp[i + data[i][0]] else dp[i + data[i][0]]
    dp[i + 1] = dp[i] if dp[i] > dp[i + 1] else dp[i + 1]
print(data)
print(dp)
print(max(dp))
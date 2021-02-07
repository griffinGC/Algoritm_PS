# 점화식
# 이전 곡의 볼륨의 값이 True라면 현재 곡의 볼륨 값을 더하고 뺀 것이 True
# dp[i][j + v[i]] = True if dp[i-1][j] = True
# dp[i][j - v[i]] = True if dp[i-1][j] = True
n, s, m = map(int, input().split())
v = [0]
v.extend(list(map(int, input().split())))
# table 생성
dp = [[False] * (m + 1) for _ in range(n + 2)]
# 맨처음은 임의로 셋팅해주기
dp[1][s] = True
# n + 1 까지 되어야 n번째 껏 까지 모두 반영 됨
for i in range(2, n + 2):
    for j in range(m + 1):
        if dp[i - 1][j] == True:
            if j + v[i - 1] <= m:
                dp[i][j + v[i - 1]] = True
            if j - v[i - 1] >= 0:
                dp[i][j - v[i - 1]] = True

for i in range(m, -1, -1):
    if dp[n + 1][i] == True:
        print(i)
        exit(0)
        break
print(-1)
import sys
input = sys.stdin.readline

data = list()
# data.append((0,0))
n = int(input())
for _ in range(n):
    a,b = map(int, input().split())
    # 튜플로 넣음
    data.append((a,b))

def solution(n, data):
    len_data = len(data)
    # 2차원 배열로 생성
    tabulate_table = [[0 for i in range(n + 1)] for j in range(len_data + 1)]
    for i in range(len_data + 1):
        for w in range(n + 1):
            # print("data[i][0], ", data[i][0])
            # print("w", w)

            if i == 0 or w == 0:
                tabulate_table[i][w] = 0
            # i는 원소 index 0은 앞에 있는 기간
            elif data[i-1][0] <= w:
                # w는 day
                tabulate_table[i][w] = max(data[i-1][1] + tabulate_table[i-1][w - data[i-1][0]], tabulate_table[i-1][w])
            else:
                tabulate_table[i][w] = tabulate_table[i][w]
    return tabulate_table[len_data][n]

print(data)
result = solution(n, data)

print(result)

################################################
# 순차적으로 채워 나가는 형태
# https://velog.io/@skyepodium/%EB%B0%B1%EC%A4%80-14501-%ED%87%B4%EC%82%AC-exjyfr5vgj#2-%EC%8B%9C%EA%B0%84%EC%95%88%EC%97%90-%EC%B6%A9%EB%B6%84%ED%9E%88-%ED%92%80%EA%B3%A0-%EC%8B%9C%EA%B0%84%EC%9D%B4-%EB%82%A8%EC%95%84%EB%8F%95%EB%8B%88%EB%8B%A4
n = int(input())
t, p = [0], [0]
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
dp = [0] * (n + 2)
for i in range(1, n + 1):
    # 추가할 경우
    # n번째 일에 기간이 1인 값이 들어올 수 있기 때문에 n+1 과 같거나 작은것까지 고려!
    if i + t[i] <= (n + 1):
        dp[i + t[i]] = max(dp[i] + p[i], dp[i + t[i]])
    # 추가하지 않을 경우
    dp[i + 1] = max(dp[i + 1], dp[i])
print(dp)
print(max(dp))


####################################################
# 뒤에서 앞으로 채워나가는 형태
import sys
n = int(sys.stdin.readline().strip())
t = [0] * (n + 1)
p = [0] * (n + 1)
dp = [0] * (n + 2)

for i in range(1, n + 1):
    t[i], p[i] = map(int, sys.stdin.readline().strip().split(" "))

for i in range(n, 0, -1):
    next = i + t[i]

    dp[i] = dp[i + 1] if next > n + 1 else max(dp[i + 1], dp[next] + p[i])

print(dp[1])
#####################################################

# 거꾸로 채워 나가는 형태
import sys
n = int(sys.stdin.readline().strip())
t = [0] * (n + 1)
p = [0] * (n + 1)
dp = [0] * (n + 1)
for i in range(n):
    t[i], p[i] = map(int, sys.stdin.readline().strip().split(" "))
    dp[i] = p[i]

for i in range(n - 1, -1, -1):
    # 초과할경우 이전의 값을 그대로 가져옴
    if t[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
print(dp[0])

##################################################
# 거꾸로 채워 나가는 형태
import sys
n = int(sys.stdin.readline().strip())
t = [0] * (n + 1)
p = [0] * (n + 1)
dp = [-1] * (n + 2)

for i in range(1, n + 1):
    t[i], p[i] = map(int, sys.stdin.readline().strip().split(" "))

def dfs(i):
    if i > n:
        return 0
    if dp[i] == -1:
        dp[i] = dfs(i + 1)
        if i + t[i] <= (n + 1):
            dp[i] = max(dp[i], p[i] + dfs(i + t[i]))
    return dp[i]

ans = dfs(0)
print(ans)
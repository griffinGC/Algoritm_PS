# https://kyu9341.github.io/algorithm/2020/03/11/algorithm14226/
# https://developingbear.tistory.com/138
# https://devbelly.tistory.com/108
# 이모티콘 s개 생성
# 3가지 연산 이용
# bfs 이용 => visited를 이모티콘 방문 여부 2차원 배열 => 이모티콘의 수 와 클립보드에 저장된 이모티콘의 갯수를 이용
from collections import deque
s = int(input())
q = deque()
# visited[이모티콘의 수][클리보드의 이모티콘 수]
visited = [[False] * 1001 for _ in range(1001)]
visited[1][0] = True
# 이모티콘의 수, 클립보드의 수, 시간
q.append((1, 0, 0))
while q:
    e, clip, t = q.popleft()
    if e == s:
        print(t)
        exit(0)

    if 0 < e < 1001:
        if visited[e][e] is False:
            visited[e][e] = True
            q.append((e, e, t + 1))
        # clip이 0 이상 조건이 필요없음 어차피 위에서 e가 0보다 큰걸로 조건 수행했으므로
        if e + clip < 1001 and visited[e + clip][clip] is False:
            visited[e + clip][clip] = True
            q.append((e + clip, clip, t + 1))
        # e가 1000을 넘을때만 수행하는 것이 아닌 모든 경우에 대해서 탐색을 하기 위해서 e에 대한 조건을 걸지 않음
        if visited[e - 1][clip] is False:
            visited[e - 1][clip] = True
            q.append((e - 1, clip, t + 1))

####

# https://devbelly.tistory.com/108
s = int(input())
# 그냥 range에 넣고 돌림으로써 각각 하나씩 추가한 것을 의미 => 즉 최대의 경우
# 여기서는 계속해서 이모티콘을 무한으로 복사하는 것은 고려하지 않았네
time = list(range(1001))
# i 상태에서 갱신할 수 있는 상태는 i의 배수 상태
# i를 복사한 후에 계속 붙여넣기 하면 계속 i의 배수들에 영향을 끼칠 수 있음

# 상향식 dp
for i in range(2, 1001):
    j = 2
    while i * j <= 1001:
        # time[i] + j 는 i는 현재 클립보드에 있는 갯수를 뜻하고 j는 반복된 횟수를 뜻하는 듯
        # 곱한 값에다가 곱한값과 time[i] 값에 j 더한것 비교
        time[i * j] = min(time[i * j], time[i] + j)
        # 곱한 값에서 1 뺀것과, 곱한 값에서 1 더한것 비교
        time[i * j - 1] = min(time([i * j - 1], time[i * j] + 1))
        j + 1



# 플로이드 와샬 사용
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
table = [[float('inf')] * n for _ in range(n)]
dp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            table[i][j] = 0


for _ in range(m):
    a, b, c = map(int, input().split())
    table[a - 1][b - 1] = c
    table[b - 1][a - 1] = c
    dp[a - 1][b - 1] = b
    dp[b - 1][a - 1] = a

for _ in dp:
    print(_)
print()
for k in range(n):
    for i in range(n):
        for j in range(n):
            if table[i][k] + table[k][j] < table[i][j]:
                table[i][j] = table[i][k] + table[k][j]
                # 경유하는 곳을 적어줌
                dp[i][j] = dp[i][k]
                for _ in dp:
                    print(_)
                print()

for i in range(n):
    for j in range(n):
        if i == j:
            print("-", end=" ")
        else:
            print(dp[i][j], end=" ")
    print()
##############################################################
# 다익스트라 사용
import sys
from heapq import heappop, heappush
from collections import defaultdict
# 다익스트라와 역추적을 이용한 풀이
input = sys.stdin.readline
# n은 node 갯수, m은 edge 갯수
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    v1, v2, cost = map(int, input().split())
    graph[v1].append((cost, v2))
    graph[v2].append((cost, v1))

# 매 행마다 다익스트라 진행
def dijkstra_print(s):
    dist = [float('inf')] * (n + 1)
    dist[s] = 0
    trace = [0] * (n + 1)
    q = []
    heappush(q, (0, s))
    while q:
        cost, now = heappop(q)
        if dist[now] < cost:
            continue
        for c, v in graph[now]:
            # c는 값, v는 노드
            if c + cost < dist[v]:
                dist[v] = c + cost
                # 다음노드로 가는 값에다가는 지금 값 삽입
                # 예를 들어 trace[1] = 2 라는 것은 2가 최단 거리로 가기 위해서는 1을 거쳐서 가야함
                trace[v] = now
                heappush(q, (c + cost, v))
    for i in range(1, n + 1):
        if i == s:
            print("-", end=" ")
        elif trace[i] == s:
            print(i, end=" ")
        else:
            index = i
            while True:
                if trace[index] == s:
                    print(index, end=" ")
                    break
                else:
                    index = trace[index]


for i in range(1, n +1):
    dijkstra_print(i)
    print()



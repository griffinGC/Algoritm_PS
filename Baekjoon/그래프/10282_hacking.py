import heapq
import sys
input = sys.stdin.readline

# 2
# 3 2 2 => 첫째 줄에 컴퓨터 개수 n, 의존성 개수 d, 해킹당한 컴퓨터의 번호 c
# 2 1 5 => 정수 a, b, s / 컴퓨터 a가 컴퓨터 b를 의존하며, 컴퓨터 b가 감염되면 s초 후 컴퓨터 a도 감염됨을 뜻한다.
# 3 2 5

# 3 3 1
# 2 1 2
# 3 1 8
# 3 2 4

def dijkstra(start):
    heap_date = []
    heapq.heappush(heap_date, (0, start))
    distance[start] = 0
    while heap_date:
        dist, now = heapq.heappop(heap_date)
        if distance[now] < dist:
            continue
        for i in adj[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap_date, (cost, i[0]))


for _ in range(int(input())):
    vertex, edge, com = map(int, input().split())
    distance = [1e9] * (vertex + 1)
    adj = [[] for i in range(vertex + 1)]
    for _ in range(edge):
        a, b, cost = map(int, input().split())
        # 감염원은 b -> b 감염시 cost초 뒤에 a 감염
        adj[b].append((a, cost))
    dijkstra(com)
    count = 0
    max_distance = 0
    for i in distance:
        if i != 1e9:
            count += 1
            if i > max_distance:
                max_distance = i
    print(count, max_distance)

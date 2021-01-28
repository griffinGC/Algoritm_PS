# Kruskal version
import sys
from collections import defaultdict
input = sys.stdin.readline
v, e = map(int, input().split())
# 그래프
g = defaultdict(list)
edges = []
for _ in range(e):
    v1, v2, c = map(int, input().split())
    edges.append((c, v1-1, v2-1))
# union find를 위한 rank와 parent
parent = [i for i in range(v)]
rank = [0 for i in range(v)]
def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
def union(x, y):
    r1 = find(x)
    r2 = find(y)
    if rank[r1] > rank[r2]:
        parent[r2] = r1
    else:
        parent[r1] = r2
        if rank[r1] == rank[r2]:
            rank[r2] += 1
val = 0
def kruskal():
    global val
    edges.sort()
    # 정렬을 하고 가장 작은것 부터 뽑아 옴
    for edge in edges:
        cost, node1, node2 = edge
        # 부모가 같지 않을 경우 집합을 합침
        if find(node1) != find(node2):
            print(parent)
            union(node1, node2)
            val += cost
    print(parent)
    return val
print(kruskal())
######################################################################################################################
# Prim version
# https://makefortune2.tistory.com/37
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
v, e = map(int, input().split())
# e개의 입력
# 튜플의 리스트로 저장하는데 (가중치, 노드)
# 양방향 넣어 줘야 함
d = defaultdict(list)
for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(d[a], (c, b))
    heapq.heappush(d[b], (c, a))

val = 0
# priority Queue 이용
q = []
nodes = {1}
q.extend(d[1])
while q:
    cost, des = heapq.heappop(q)
    if des in nodes:
        continue
    nodes.add(des)
    val += cost
    for edge in d[des]:
        if edge[1] not in nodes:
            heapq.heappush(q, edge)
print(val)
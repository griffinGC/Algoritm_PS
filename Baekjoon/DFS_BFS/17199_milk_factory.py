# 결국 모든 노드가 다 방문하게 되는 곳을 찾는 것
import sys
input = sys.stdin.readline
from collections import defaultdict
from collections import deque
n = int(input())
outdegree = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    outdegree[a].append(b)
q = deque()
arr = [0] * (n + 1)
arr[0] = -1
for i in range(1, n + 1):
    q.append(i)
    visited = [0] * (n + 1)
    visited[i] = 1
    while q:
        now = q.popleft()
        for j in outdegree[now]:
            if visited[j] == 0:
                visited[j] += 1
                q.append(j)
    for k in range(1, len(visited)):
        if visited[k] == 1:
            arr[k] += 1
for i in range(1, len(arr)):
    if arr[i] == n:
        print(i)
        exit(0)
print(-1)
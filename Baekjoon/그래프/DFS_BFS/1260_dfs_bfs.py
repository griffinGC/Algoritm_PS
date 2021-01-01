import sys
from collections import deque
input = sys.stdin.readline
node, edge, start = map(int, input().split())
print(node, edge, start)
adj = dict()
for i in range(edge):
    v1, v2 = map(int, input().split())
    if v1 not in adj:
        adj[v1] = list()
    if v2 not in adj:
        adj[v2] = list()
    adj[v1].append(v2)
    adj[v2].append(v1)

print(adj)

def dfs(start, adj):
    st = list()
    visited = []
    result = list()
    st.append(start)
    while st:
        node = st.pop()
        if node in visited:
            continue
        visited.append(node)
        # print("node", node)
        result.append(node)
        for i in reversed(adj[node]):
            if i not in visited:
                st.append(i)
    return result
ans = dfs(start, adj)
print("ans", ans)

def bfs(start, adj):
    q = deque()
    visited = list()
    q.append(start)
    result = []
    while q:
        node = q.popleft()
        if node in visited:
            continue
        visited.append(node)
        result.append(node)
        for i in adj[node]:
            if i not in visited:
                q.append(i)
    return result

ans2 = bfs(start, adj)
print("ans2", ans2)

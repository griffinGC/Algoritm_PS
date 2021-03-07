from collections import deque
from collections import defaultdict
def solution(n, edge):
    ans = 0
    result_list = defaultdict(list)
    graph = defaultdict(list)
    for data in edge:
        a, b = data
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (n + 1)
    def bfs(start):
        q = deque([(start, 0)])
        visited[start] = True
        while q:
            now, cnt = q.popleft()
            for i in graph[now]:
                if visited[i] is False:
                    visited[i] = True
                    q.append((i, cnt + 1))
                    result_list[cnt + 1].append(i)
    bfs(1)
    for i in range(n, -1, -1):
        if i in result_list and len(result_list[i]) > 0:
            ans = len(result_list[i])
            break
    return ans

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
ans = solution(n, vertex)
print(ans)
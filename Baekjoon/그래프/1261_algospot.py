# bfs 이용하여서 업데이트 시키는 형태로 진행
# 0 이면 아무것도 더하지 않고 이전의 값 덮어 씌움
# 1이면 더하기
# 만약 이미 방문했다면 값을 비교
# 상하 좌우로 이동하는것 고려해야 함 무한루프에 빠지면 안되도록 만들어야 함 => 4 이상일 경우는 이제 방문 못하도록 만들어야 함

# 행은 m 열은 n
from collections import deque
n, m = map(int, input().split())
maze = []
mv = ((0, 1), (1, 0), (0, -1), (-1, 0))
for _ in range(m):
    maze.append(list(map(int,input().strip())))
visited = [[0] * n for _ in range(m)]
result = [[0] * n for _ in range(m)]
q = deque()
# x, y, 값
q.append((0, 0, 0))
visited[0][0] = 1
while q:
    x, y, v = q.popleft()
    if x == m - 1 and y == n - 1:
        print(v)
        break
    for mx, my in mv:
        nx = x + mx
        ny = y + my
        if 0 <= nx < m and 0 <= ny < n:
            if visited[nx][ny] != 0:
                continue
            visited[nx][ny] = 1
            if maze[nx][ny] == 1:
                result[nx][ny] = v + 1
                q.append((nx, ny, v + 1))
            else:
                q.appendleft((nx, ny, v))

#######
# heap 이용한 방식
n, m = map(int, input().split())
maze = []
mv = ((0, 1), (1, 0), (0, -1), (-1, 0))
for _ in range(m):
    maze.append(list(map(int,input().strip())))
visited = [[0] * n for _ in range(m)]
result = [[0] * n for _ in range(m)]
q = []
heapq.heappush(q, (0, 0, 0))
while q:
    v, x, y = heapq.heappop(q)
    if x == m - 1 and y == n - 1:
        print(v)
        exit(0)
    if visited[x][y] != 0:
        continue
    visited[x][y] += 1
    if maze[x][y] == 1:
        nv = v + 1
    else:
        nv = v
    for mx, my in mv:
        nx = x + mx
        ny = y + my
        if 0 <= nx < m and 0 <= ny < n:
            heapq.heappush(q, (nv, nx, ny))
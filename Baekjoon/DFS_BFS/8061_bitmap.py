import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
pixels = []
d = [[-1] * m for _ in range(n)]
for _ in range(n):
    pixels.append(input().strip())
mv = [(1, 0), (-1, 0), (0, 1), (0, -1)]
q = deque()
def bfs():
    while q:
        x, y, cnt = q.popleft()
        if d[x][y] != -1:
            continue
        d[x][y] = cnt
        for mx, my in mv:
            nx = x + mx
            ny = y + my
            if 0 <= nx < n and 0 <= ny < m:
                q.append((nx, ny, cnt + 1))
for i in range(n):
    for j in range(m):
        # 시간 초과 막기 위함
        if pixels[i][j] == '1':
            q.append((i, j, 0))
bfs()
for _ in d:
    print(" ".join(map(str,_)))
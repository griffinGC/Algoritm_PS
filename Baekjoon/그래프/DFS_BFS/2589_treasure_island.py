from collections import deque
r , c = map(int, input().split())
t_map = list()
dxdy = ((0, 1), (0, -1), (1, 0), (-1, 0))
for _ in range(r):
    t_map.append(list(input().strip()))
count = 0
for i in range(r):
    for j in range(c):
        if t_map[i][j] == 'L':
            number = 0
            visited = [[0 for _ in range(c)] for _ in range(r)]
            q = deque([(i, j, 0)])
            while len(q) > 0:
                cur_x, cur_y, cur_dis = q.popleft()
                if visited[cur_x][cur_y] == 1: continue
                visited[cur_x][cur_y] = 1
                for dx, dy in dxdy:
                    mvX, mvY = cur_x + dx, cur_y + dy
                    if 0 <= mvX < r and 0 <= mvY < c and visited[mvX][mvY] == 0 and t_map[mvX][mvY] == 'L':
                        q.append((mvX, mvY, cur_dis + 1)); number = max(number, cur_dis + 1)
            count = max(count, number)
print(count)
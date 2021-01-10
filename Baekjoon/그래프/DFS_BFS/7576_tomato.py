from collections import deque
c, r = map(int, input().split())
tomato_box = list()
move = [(0, -1), (1, 0), (0, 1), (-1, 0)]
for _ in range(r):
    tomato_box.append(list(map(int, input().split())))
days = 0
reap_queue = deque()
for row in range(r):
    for col in range(c):
        if tomato_box[row][col] == 1:
            reap_queue.append((row, col))
# bfs
while reap_queue:
    s_r, s_c = reap_queue.popleft()
    for x, y in move:
        mv_x, mv_y = s_r + x, s_c + y
        if 0 <= mv_x < r and 0 <= mv_y < c and tomato_box[mv_x][mv_y] == 0:
            reap_queue.append((mv_x, mv_y))
            tomato_box[mv_x][mv_y] = tomato_box[s_r][s_c] + 1
for row in tomato_box:
    if 0 in row:
        print(-1)
        exit(0)
    for j in row:
        if j > days:
            days = j
print(days - 1)

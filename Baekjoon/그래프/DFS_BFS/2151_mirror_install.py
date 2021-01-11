from collections import deque
n = int(input())
home_map = list()
di, dj = [[1, -1], [0, 0]], [[0, 0], [1, -1]]
# [x][y][dir]
visited = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(2)]
for _ in range(n):
    home_map.append(input())
def bfs(x, y):
    move_queue = deque()
    # 카운트, 방향, 좌표 => 3가지 넣어줌
    move_queue.append((0, 0, x, y))
    move_queue.append((0, 1, x, y))
    while move_queue:
        cnt, dire, i, j = move_queue.popleft()
        # 가져온 곳에 거울이 설치 되므로 굴절시키기 위해 방향 전환 => 굴절된 방향으로 방문한적 있는지 체크 후, 없다면 방문 처리 후, 시작
        if visited[1 - dire][i][j]:
            continue
        visited[1-dire][i][j] = 1
        # 방향을 위해 2번만 수행
        for m in range(2):
            dx, dy = i, j
            while True:
                # queue에 들어간 것들은 모두 ! 이기 때문에 빛이 굴절되어 방향을 꺽어야만함 -> 1-dire로 방향 전환된 상태로 계속 전진하며 체크
                # while문안에 있기 때문에 앞으로 갔다가 뒤로 가지 않고, 조건식을 만족하게 되면 계속해서 전진
                dx, dy = dx + di[1 - dire][m], dy + dj[1 - dire][m]
                if not (0 <= dx < n and 0 <= dy < n):
                    break
                # 더이상 전진 불가하기 때문
                if home_map[dx][dy] == "*":
                    break
                if home_map[dx][dy] == "#":
                    print(cnt)
                    return
                if home_map[dx][dy] == "!":
                    move_queue.append((cnt + 1, 1-dire, dx, dy))
                visited[1-dire][dx][dy] = 1

for a in range(n):
    for b in range(n):
        # 시작점
        if home_map[a][b] == '#':
            t1, t2 = a, b
bfs(t1, t2)



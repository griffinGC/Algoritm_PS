from collections import deque
w, h = map(int, input().split())
wide_map = list()
# 기본 맵을 둘러싸도록 생성
wide_map.append([0 for _ in range(w + 2)])
for _ in range(h):
    wide_map.append([0] + list(map(int, input().split()))+ [0])
wide_map.append([0 for _ in range(w + 2)])
ans = 0

# dfs
def solution():
    global ans
    # 움직이는 방향
    mx = [1, 1, 0, 0, -1, -1]
    my = [[-1, 0, -1, 1, -1, 0], [0, 1, -1, 1, 0, 1]]
    def bfs(i, j):
        global ans
        q = deque()
        q.append((i, j))
        while len(q) > 0:
            x, y = q.popleft()
            if wide_map[x][y] == -1:
                continue
            wide_map[x][y] = -1
            for k in range(6):
                now_x = x + mx[k]
                now_y = y + my[x & 1][k]
                if 0 <= now_x < h + 2 and 0 <= now_y < w + 2:
                    if wide_map[now_x][now_y] == 0:
                        q.append((now_x, now_y))
                    elif wide_map[now_x][now_y] == 1:
                        ans += 1
    bfs(0,0)
    return ans

# bfs
def solution():
    global ans
    # 움직이는 방향
    mx = [1, 1, 0, 0, -1, -1]
    my = [[-1, 0, -1, 1, -1, 0], [0, 1, -1, 1, 0, 1]]
    def dfs(i, j):
        global ans
        wide_map[i][j] = -1
        for k in range(6):
            now_x = i + mx[k]
            now_y = j + my[i & 1][k]
            if 0 <= now_x < h + 2 and 0 <= now_y < w + 2:
                if wide_map[now_x][now_y] == 0:
                    dfs(now_x, now_y)
                elif wide_map[now_x][now_y] == 1:
                    ans += 1
    dfs(0,0)
    return ans
result = solution()
print(result)

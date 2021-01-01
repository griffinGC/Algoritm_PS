from collections import deque
import copy
def bfs(vsd, i, j):
    q = deque()
    q.append((i, j))
    while len(q) > 0:
        x, y = q.popleft()
        if vsd[x][y] == 1:
            continue
        vsd[x][y] = 1
        for dx, dy in mv:
            mx, my = x + dx, y + dy
            if 0 <= mx < r and 0 <= my < c and vsd[mx][my] == 0 and ice[mx][my] > 0:
                    q.append((mx, my))
ice = list()
r, c = map(int, input().split())
for _ in range(r):
    ice.append(list(map(int, input().split())))
mv = ((0, 1), (0, -1), (1, 0), (-1, 0))
y = 0
a_z = False
while a_z is False:
    vsd = [[0]*c for _ in range(r)]
    cnt = 0
    for i in range(r):
        for j in range(c):
            if vsd[i][j] == 0 and ice[i][j] > 0:
                bfs(vsd, i, j)
                cnt += 1
    if cnt > 1:
        break
    b_ice = copy.deepcopy(ice)
    for i in range(r):
        for j in range(c):
            if b_ice[i][j] > 0:
                del_c = 0
                for dx, dy in mv:
                    mx, my = dx + i, dy + j
                    if b_ice[mx][my] == 0:
                        del_c += 1
                ice[i][j] -= del_c
                if ice[i][j] < 0:
                    ice[i][j] = 0
    a_z = True
    for i in range(r):
        for j in range(c):
            if ice[i][j] != 0:
                a_z = False
                break
    y += 1
if a_z:
    y = 0
print(y)
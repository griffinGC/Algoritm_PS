from collections import defaultdict
r, c = map(int, input().split())
maps = [input() for _ in range(r)]
mv = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = 0
alphabets = defaultdict(int)
def dfs(i, j, cnt):
    global ans
    ans = max(ans, cnt)
    for mx, my in mv:
        nx, ny = i + mx, j + my
        if 0 <= nx < r and 0 <= ny < c and alphabets[maps[nx][ny]] == 0:
            alphabets[maps[nx][ny]] += 1
            cnt += 1
            dfs(nx, ny, cnt)
            alphabets[maps[nx][ny]] -= 1
            cnt -= 1
alphabets[maps[0][0]] += 1
dfs(0, 0, 1)
print(ans)

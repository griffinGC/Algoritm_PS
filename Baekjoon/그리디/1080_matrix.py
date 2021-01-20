import sys
input = sys.stdin.readline
n, m = map(int, input().split())
checked = [[False] * m for _ in range(n)]
a = [list(map(int, input().strip())) for _ in range(n)]
b = [list(map(int, input().strip())) for _ in range(n)]
diff = 0
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            checked[i][j] = True
            diff += 1
if diff == 0:
    print(0)
    exit(0)
if n < 3 or m < 3:
    print(-1)
    exit(0)
cnt = 0
def reverse(mx, my):
    global cnt
    for x in range(3):
        for y in range(3):
            checked[mx + x][my + y] = not checked[mx + x][my + y]
    cnt += 1
for i in range(n - 2):
    for j in range(m - 2):
        if j == m - 3:
            if not(checked[i][j] == checked[i][j + 1] and checked[i][j] == checked[i][j + 2]):
                print(-1)
                exit(0)
        if i == n - 3:
            if not (checked[i][j] == checked[i + 1][j] and checked[i][j] == checked[i + 2][j]):
                print(-1)
                exit(0)
        if checked[i][j] is True:
            reverse(i, j)
final_check = checked[n - 3][m - 3]
for i in range(n - 3, n):
    for j in range(m-3, m):
        if checked[i][j] != final_check:
            print(-1)
            exit(0)
print(cnt)

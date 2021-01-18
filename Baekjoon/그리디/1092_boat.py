import sys
input = sys.stdin.readline
n = int(input())
crane = sorted(list(map(int, input().split())), reverse=True)

m = int(input())
box = sorted(list(map(int, input().split())), reverse=True)
checked = [False] * m
pos = [0] * n
result, cnt = 0, 0

if crane[0] < box[0]:
    print(-1)
    exit(0)

while cnt < len(box):
    # 박스보다 크레인이 갯수가 작으므로 크레인을 돌리는 형식으로 구현 && 박스를 처음부터 돌리지 않고 크레인이 이전에 있었던 곳부터 다시 돌림
    for i in range(n):
        while pos[i] < len(box):
            if not checked[pos[i]] and crane[i] >= box[pos[i]]:
                checked[pos[i]] = True
                pos[i] += 1
                cnt += 1
                break
            pos[i] += 1
    result += 1
print(result)
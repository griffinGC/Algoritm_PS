import sys
input = sys.stdin.readline
cube = [0] * 20
def solution():
    l, w, h = map(int, input().split())
    n = int(input().strip())
    data = []
    for _ in range(n):
        # 큐브에다가 갯수를 일단 넣음
        i, nu = map(int, input().split())
        cube[i] = nu
    before = 0
    cnt = 0
    for i in range(n - 1, -1, -1):
        # 2^3 으로 이동하기 때문 2 * 2 * 2 이기 때문
        before <<= 3
        # print(before)
        # (l >> i ) * ( w >> i ) * (h >> i) 가 before보다 작을 수 없음
        # 현재 총 가능한 큐브 크기 - 이전에 들어갔던 블럭들 크기
        possible_cube = (l >> i) * (w >> i) * (h >> i) - before
        # print((l >> i), (w >> i), (h >> i))
        # 넣을 수 있는 큐브와 현재 가지고 있는 큐브의 갯수중 작은 것 선택
        new = min(cube[i], possible_cube)
        before += new
        cnt += new
    if before != l*w*h:
        print(-1)
    else:
        print(cnt)
solution()
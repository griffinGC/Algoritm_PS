n = int(input())
cnt = 0
# 직접 지도를 만들 필요 없이
# 각각의 행에 있는 퀸이 위치하는 열을 나타내는 배열 생성 => 1차원 배열
rows = [0] * n
def check(x):
    # 이전행들과 비교하며 수행
    for i in range(x):
        if rows[x] == rows[i] or abs(rows[x] - rows[i]) == x - i:
            return False
    return True

# x는 행의 위치를 뜻함
def find_queen(x):
    global cnt
    # n 번재 행까지 도달할때까지 수행
    if x == n:
        cnt += 1
    else:
        for i in range(n):
            # x 번째 행에 i 번째 열의 위치에 계속 퀸을 업데이트 하며 놓아봄
            rows[x] = i
            if check(x):
                find_queen(x + 1)
find_queen(0)
print(cnt)
# 조합문제
n, m = map(int, input().split())
arr = [0] * m
def comb(index, cnt):
    if cnt == m:
        print(" ".join(map(str, arr)))
        return
    # 처음부터가 아닌 그 자리부터 다시 시작 함으로써 조합 가능하게 해줌
    for i in range(index, n):
        arr[cnt] = i + 1
        comb(i + 1, cnt + 1)
        # 순열에서는 visited가 필요하지만 조합에서는 필요 없음
        # visited[i] = False
comb(0, 0)
# 조합을 구하는 문제
# k 개의 수를 골라 집합 s를 만든 다음 그 수만 가지고 번호를 선택하는 것
# k 개의 수를 가지고 6개를 가진 집합을 생성
# 수를 모두 고르는 방법을 구하면 됨
def comb(index, total, arr, origin, cnt):
    if cnt == 6:
        print(" ".join(map(str, arr)))
        return
    for i in range(index, total):
        # 조합이기 때문에 visited는 필요 없음
        arr[cnt] = origin[i]
        comb(i + 1, total, arr, origin, cnt + 1)

while True:
    number = list(map(int, input().split()))
    if number[0] == 0:
        exit(0)
    temp = [0] * 6
    comb(0, number[0], temp, number[1:], 0)
    print()
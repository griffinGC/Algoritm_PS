# m이 필요한 나무의 길이
n, m = map(int, input().split())
# 나무의 높이들
# 그냥 이진 탐색과 크게 다를 바 없음
trees = list(map(int, input().split()))
# 굳이 정렬하지 않음 => 정렬하는데 시간이 많이 소요되기 때문
right = max(trees)
left = 0
ans = 0
while left <= right:
    mid = (left + right) // 2
    total = 0
    for t in trees:
        if t > mid:
            total += t - mid
    # 이부분이 결정문제이기때문에 파라메트릭 서치라고 볼 수 있음
    if total >= m:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)
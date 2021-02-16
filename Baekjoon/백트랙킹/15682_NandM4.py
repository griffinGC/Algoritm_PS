# 길이가 m인 수열을 모두 구하는 프로그램
# 같은 수를 여러번 골라도 됨
# 고른 수열은 비 내림차순 (즉, 오름차순)
import sys
# sys.setrecursionlimit(1000000)
n, m = map(int, input().split())
max_index = 9
arr = [0] * max_index
visited = [False] * max_index
def backtracking(num, cnt):
    global arr
    if cnt == m:
        for i in range(m):
            print(arr[i], end=" ")
        print()
        return
    for i in range(num, n + 1):
        # 중복으로 출력되어도 되기 때문에 cnt자리에 i 삽입
        arr[cnt] = i
        backtracking(i, cnt + 1)
backtracking(1, 0)

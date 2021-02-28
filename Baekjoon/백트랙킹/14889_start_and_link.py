# 백트래킹 사용
# 종료 조건은 2/n 이 되었을때
# visited만 더하고, 그 외에만 더하고 하는 형식으로 해서 수행
n = int(input())
val = [ list(map(int, input().split())) for _ in range(n)]
mid = n // 2
team1 = [-1] * mid
min_diff = float('inf')
def backtracking(cnt, index):
    global min_diff
    if cnt == mid:
        # 각각의 값 더하기
        team1_val, team2_val = 0, 0
        team2 = [i for i in range(n) if i not in team1]
        # 시간을 줄이기 위해 index를 사용
        for i in range(0, len(team1) - 1):
            for j in range(i + 1, len(team1)):
                team1_val += val[team1[i]][team1[j]] + val[team1[j]][team1[i]]

        for i in range(0, len(team2) - 1):
            for j in range(i + 1, len(team2)):
                team2_val += val[team2[i]][team2[j]] + val[team2[j]][team2[i]]
        # 두 값의 차를 계산
        min_diff = min(abs(team1_val - team2_val), min_diff)
        return
    for i in range(index, n):
        team1[cnt] = i
        backtracking(cnt + 1, i + 1)
backtracking(0, 0)
print(min_diff)
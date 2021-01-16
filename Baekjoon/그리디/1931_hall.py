import sys
input = sys.stdin.readline
n = int(input())
hall_list = list()
min_s, max_e = 0, 0
for _ in range(n):
    s, e = map(int, input().split())
    # (시작, 종료)
    hall_list.append((s, e))
# print(hall_list)
# 일단 먼저 끝나는애를 기준으로 잡고, 그 다음으로 시작점을 기준으로 잡음
# 시적점으로 기준을 다시 잡는 이유는 같은 회의의 시작시간과 끝나는 시간이 같을수도 있기 때문
hall_list = sorted(hall_list, key=lambda x: (x[1], x[0]))
# print(hall_list)
# 그리디 로 작성
# 가장 빨리 종료되는 것부터 정렬
# 먼저 끝나는것이 무엇이든간에 상관없음, 중요한 것은 다음에 시작되는 시간 전에 끝나야 그것을 카운트 할 수 있는 것임
end, cnt = 0, 0
for time in hall_list:
    if end <= time[0]:
        cnt += 1
        end = time[1]
print(cnt)
# 만나이, 세는 나이, 연나이
# 만나이 => 생일지나는 여부에 따른 나이
# 세는 나이 => 태어났을때 1세 -> 일반적으로 세는 나이
# 연나이 => 법률적으로 일괄적으로 하는 나이 -> 1월1일 부터 1세 추가
birth = list(map(int, input().split()))
end = list(map(int, input().split()))
gap = end[0] - birth[0]


def solution(b_date, now, diff):
    cal_result = [diff for _ in range(3)]
    # 만나이
    # 월을 보고 일을 봐야함
    cal_result[0] -= 1
    if b_date[1] < now[1] or (b_date[1] == now[1] and b_date[2] <= now[2]):
        cal_result[0] += 1
    elif cal_result[0] < 0:
        cal_result[0] = 0
    cal_result[1] += 1
    return cal_result


result = solution(birth, end, gap)

for r in result:
    print(r)

## short
# b = list(map(int, input().split()))
# now = list(map(int, input().split()))
# gap = now[0] - b[0]
# cal = gap - 1
# if b[1] < now[1] or (b[1] == now[1] and b[2] <= now[2]):
#     cal += 1
# cal = 0 if cal < 0 else cal
# print(cal)
# print(gap + 1)
# print(gap)
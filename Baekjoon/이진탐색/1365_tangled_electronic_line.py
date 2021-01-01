import bisect
number = int(input())
number_list = list(map(int, input().split()))

# LIS(Longest Increase Sequence) 사용
# 전체에서 LIS 빼기
def solution():
    lis_list = list()
    for idx, val in enumerate(number_list):
        if idx == 0:
            lis_list.append(val)1365
            continue
        if val > lis_list[-1]:
            lis_list.append(val)
        else:
            bisect_idx = bisect.bisect_left(lis_list, val)
            lis_list[bisect_idx] = val
    cut_point = len(number_list) - len(lis_list)
    return cut_point
result = solution()
print(result)
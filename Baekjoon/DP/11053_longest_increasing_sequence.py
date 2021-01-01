import sys
import bisect
# 2진탐색 사용
def solution(num_input, input_list):

    num = num_input
    result = list()
    num_list = input_list
    for i in num_list:
        if len(result) == 0:
            result.append(i)
            continue
            # 위치를 찾아서 삭제하고 다시 넣어주기
        if result[-1] < i:
            result.append(i)
        else:
            index = bisect.bisect_left(result, i)
            result[index] = i
    # print(result)
    return len(result)

def solution2(num_input, input_list):
    num = num_input
    num_list = [0]
    num_list += input_list
    dp = [0 for i in range(int(num) +1)]
    max = 0
    for i in range(1, int(num)+ 1):
        min = 0
        for j in range(0, i):
            if num_list[i] > num_list[j]:
                if min < dp[j]:
                    min = dp[j]
        dp[i] = min + 1

        if max < dp[i]:
            max = dp[i]

    print(dp)
    return max

input = sys.stdin.readline
num = input()
num_list = [i for i in list(map(int, input().split()))]

result = solution(num, num_list)
result2 = solution2(num, num_list)
print(result)
print(result2)
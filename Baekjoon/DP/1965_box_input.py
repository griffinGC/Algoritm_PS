import sys
import bisect
input = sys.stdin.readline

def solution():
    num = int(input())
    weight_list = list(map(int, input().split()))
    dp = [0 for _ in range(num)]

    for i in range(num):
        min = 0
        for j in range(0, i):
            if weight_list[i] > weight_list[j]:
                if dp[j] > min: 
                    min = dp[j]
        dp[i] = min +1

    return max(dp)

def solution2():
    num = int(input())
    weight_list = list(map(int, input().split()))
    result = list()
    for i in weight_list:
        if len(result) == 0:
            result.append(i)
            continue
        if i > result[-1]:
            result.append(i)
        else:
            index = bisect.bisect_left(result, i)
            result[index] = i
    return len(result)

result = solution()
print(result)
result = solution2()
print(result)
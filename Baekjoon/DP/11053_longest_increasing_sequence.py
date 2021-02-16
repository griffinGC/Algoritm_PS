import sys
def solution(num_input, input_list):
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
print(result)

# ---

# 가장 긴 증가하는 부분수열의 길이를 dp로 해결
n = int(input())
num = list(map(int, input().split()))
dp = [1 for _ in range(n)]
def solution2():
    # 이중 for문을 이용해서 dp로 해결
    for i in range(1, n):
        for j in range(0, i):
            if num[i] > num[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))
solution2()
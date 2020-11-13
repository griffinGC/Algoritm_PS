num = int(input())
def solution(num):
    dp = [0 for i in range(1000001)]
    before = [0 for i in range(num + 1)]
    i = 2
    while i <= num:
        # 1을 뺄 경우
        # 1로 만드는 것이기 때문에 i는 2부터 시작
        dp[i] = dp[i-1] + 1
        # 일단은 전에서 넘어온 걸로 선언해줌
        before[i] = i - 1
        if i % 2 == 0:
            # +1 해주는 이유는 전의 값에서 1 증가하기 때문
            dp[i] = min(dp[i], dp[i//2] + 1)
            # 이전것을 추적하기 위해 이전 변수로 갱신해줌
            if dp[i] == dp[i//2] + 1:
                before[i] = i//2

        if i % 3 == 0:
            # 마찬가지로 3으로 나눠질 경우 그 값번호를 포함해댜 하기 때문에 1 추가
            dp[i] = min(dp[i], dp[i//3] + 1)
            # 위와 동일하게 이전것으로 갱신
            if dp[i] == dp[i//3] + 1:
                before[i] = i//3
        
        i += 1
    print(dp[num])
    print(num, end=" ")
    end = before[num]
    # 추적하기 위한 변수를 거꾸로 추적해 나가는 방식
    while end > 0:
        print(end, end=" ")
        end = before[end]
solution(num)

# tc1 = 2
# solution(tc1)
# print()
# tc2 = 10
# solution(tc2)
# print()
# tc3 = 7
# solution(tc3)
# print()
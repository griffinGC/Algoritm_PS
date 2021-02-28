t = int(input())
def fibonacci(n):
    # 0일 경우에는 그냥 1 0 출력하고 종료
    if n == 0:
        print(1, 0)
        return
    # 1일 경우에는 그냥 0 1 출력하고 종료
    if n == 1:
        print(0, 1)
        return
    # n까지 채울 수 있도록 n + 1 크기로 초기화 시켜줌
    dp = [[0, 0] for _ in range(n + 1)]
    dp[0] = [1, 0]
    dp[1] = [0, 1]
    # 피보나치처럼 2부터 n까지 순환
    for i in range(2, n + 1):
        # # i - 1 >= 0 의미는 i에서 1을 빼도 0보다 크다면 i-1에 들어갔던 0과 1의 갯수만큼 i에서도 사용한다는 의미이기 때문에 더해줌
        # if i - 1 >= 0:
        #     dp[i][0] += dp[i - 1][0]
        #     dp[i][1] += dp[i - 1][1]
        # # i - 2 >= 0 의미는 i에서 2를 빼도 0보다 크다면 i-2에 들어갔던 0과 1의 갯수만큼 i에서도 사용한다는 의미이기 때문에 더해줌
        # if i - 2 >= 0:
        #     dp[i][0] += dp[i - 2][0]
        #     dp[i][1] += dp[i - 2][1]
        # 조건을 지정할 필요 없음 2부터 시작하기 때문에 애초에 i - 1과 i - 2의 값을 가지고 있음
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1] 
    print(" ".join(map(str, dp[n])))
for _ in range(t):
    n = int(input())
    fibonacci(n)

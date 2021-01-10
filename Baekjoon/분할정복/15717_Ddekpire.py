# 2 ^ (n -1)
n = int(input())
def solution(s):
    if s == 0:
        return 1
    ans = 1
    s -= 1
    a = 2
    # n-1 이 된 상태
    while s > 0:
        # 홀수 일때만 여기 걸림 => 짝수일때는 a 만큼을 더 곱하는 형식
        if s & 1:
            ans = ans * a % (10 ** 9 + 7)
        s = s//2
        a = a * a % (10**9 + 7)
    return ans
print(solution(n))

# 분할정복 방식 사용 => 재귀에러 발생
def pow_cal(number):
    if number == 0:
        return 1
    else:
        temp = pow_cal(number // 2)
        return (temp * temp * 2) % (10 ** 9 + 7) if number & 1 else (temp * temp) % (10 ** 9 + 7)
def solution2(s):
    return pow_cal(s-1)
print(solution2(n))
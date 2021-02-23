#### dp로도 풀 수 있음
# 문제에서 원하는 것이 경우의 수를 원하는 것이기 때문에 조합을 생각했음 => 조합은 백트래킹으로 풀 수 있음
# 백트래킹은 dp로도 풀 수 있음
n = int(input())
def cal(now):
    # 1혹은 2, 3을 빼서 0보다 작은 경우는 카운팅 하지 않고 종료
    if now < 0:
        return 0
    # now에서 빼서 0이 되는 경우만 카운팅
    elif now == 0:
        return 1
    # 백트래킹
    # 하향식
    # 1로 구성되는 경우, 2로 구성되는 경우, 3으로 구성되는 경우 => 조합으로 찾아냄
    return cal(now - 1) + cal(now - 2) + cal(now - 3)

for _ in range(n):
    num = int(input())
    ans = cal(num)
    print(ans)
# 위에서부터 아래로 쌓아가는 형태
n = int(input())
# 1번째 원소부터 파악해서 dp[1]을 제대로 업데이트 하기 위해서 맨 앞에 (0, 0, 0, 0) 넣어줌
bricks = [(0, 0, 0, 0)]
for i in range(n):
    b, h, w = map(int, input().split())
    bricks.append((i + 1, b, h, w))
# 무게순으로 정렬 => 가벼운것부터 큰것 순으로 -> 아래로 쌓아갈 수 있도록 해줌
bricks.sort(key=lambda x: x[3])
dp = [0 for i in range(n + 1)]
# for문 2개 이용하여서 해보기
# i는 정렬된 bricks의 순서를 나타냄
# 정렬된 상태이므로 무게가 작은것부터 차례차례 아래로 쌓아감
for i in range(n + 1):
    for j in range(i):
        if bricks[i][1] > bricks[j][1]:
            dp[i] = max(dp[i], dp[j] + bricks[i][2])
max_value = max(dp)
# 최대 값에서 감소해 나가는 형식으로 역추적!
index = n
result = list()
while index > 0:
    if max_value == dp[index]:
        result.append(bricks[index][0])
        max_value -= bricks[index][2]
    index -= 1
result.reverse()
print(len(result))
for i in result:
    print(i)
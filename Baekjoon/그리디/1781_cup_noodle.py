import heapq
n = int(input())
cup = list()
data = list()
# 시간내에 같은 데드라인에 있는 문제를 푸는 경우
# 현재 카운터가 데드라인보다 작은 경우 값 추가 가능
# 데드라인전에 있는 애들중에 가장 큰 애들만 넣으면 될 듯 => 데드라인의 숫자와 전체 길이 판별
for _ in range(n):
    d, noodle = map(int, input().split())
    cup.append((d, noodle))
cup.sort()
# 데드라인 작은것 부터 차례대로 순회
for deadline, cups in cup:
    heapq.heappush(data, cups)
    # if 대신 while도 가능
    if len(data) > deadline:
        heapq.heappop(data)
print(sum(data))
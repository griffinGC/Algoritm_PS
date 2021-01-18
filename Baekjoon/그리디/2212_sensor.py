def solution(sensors, k):
    sensors.sort()
    answer = 0
    # k 개로 나누는 것이니까 그 차이가 가장 큰 부분을 k-1개 만큼 없애고 나머지 부분을 더하면 됨
    dis = list()
    for i in range(len(sensors) -1):
        dis.append(sensors[i + 1] - sensors[i])
    dis.sort(reverse=True)
    for i in range(k - 1, len(dis)):
        answer += dis[i]
    return answer

n = int(input())
k1 = int(input())
sc = list(map(int, input().split()))
result = solution(sc, k1)
print(result)
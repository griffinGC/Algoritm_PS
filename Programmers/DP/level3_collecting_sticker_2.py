def solution(sticker):
    answer = 0
    if len(sticker) == 1:
        return sticker[0]
    # 처음을 넣는 것과 두번째를 넣는 것으로 나눔
    dp1 = [0 for _ in range(len(sticker))]
    dp2 = [0 for _ in range(len(sticker))]
    # 처음부터 넣는 경우
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    for i in range(2, len(sticker) - 1):
        dp1[i] = max(dp1[i - 2] + sticker[i], dp1[i - 1])
    print("dp1", dp1)
    # 두번째 부터 넣는 경우
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i - 2] + sticker[i], dp2[i - 1])
    print("dp2", dp2)
    # 두가지를 고려해서 큰 것을 리턴
    answer = max(dp1[len(sticker) - 2], dp2[len(sticker) - 1])

    return answer

input1 = [14, 6, 5, 11, 3, 9, 2, 10]
print(solution(input1))
input2 = [1, 3, 2, 5, 4]
print(solution(input2))

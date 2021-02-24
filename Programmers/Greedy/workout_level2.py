def solution(n, lost, reserve):
    # 여유분 체육복을 가지고 있지만 잃어버린 경우
    _lost = [l for l in lost if l not in reserve]
    # lost에 있는 것중에 reserve에 없는 것을 l으로 생각하고 _lost에 넣음
    _reserve = [r for r in reserve if r not in lost]
    for r in _reserve:
        # 앞은 f 뒤는 b
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

##########################################

def solution(n, lost, reserve):
    stu = [1] * n
    answer = 0
    for l in lost:
        stu[l - 1] -= 1
    for r in reserve:
        stu[r - 1] += 1
    # 맨 처음 원소만 미리 체크해줌
    if stu[0] > 1 and stu[1] < 1:
        stu[1] += 1
        stu[0] -= 1
    # 1번부터 카운팅
    for i in range(1, n):
        if stu[i] >= 2 and stu[i - 1] < 1:
            stu[i - 1] += 1
            stu[i] -= 1
        # 마지막 원소의 경우 뒤에 있는 원소 체크하지 않음
        if stu[i] >= 2 and i + 1 <= n - 1 and stu[i + 1] < 1:
            stu[i + 1] += 1
            stu[i] -= 1

    for i in range(n):
        if stu[i] >= 1:
            answer += 1
    print(stu)
    return answer
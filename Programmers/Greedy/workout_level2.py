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
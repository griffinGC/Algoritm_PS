tc = int(input())
def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
    return root[x]
def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        root[y] = x
        number[x] += number[y]

for _ in range(tc):
    n = int(input())
    root = dict()
    number = dict()
    res = []
    # 친구 관계 만으로 이동할 수 있는 cycle을 찾기를 원함
    # 즉, 2명씩 주어졌을때 2명이 친구가 되었을때 이 2명이 친구가 된 묶음임 이동할 수 있는 갯수를 뜻함
    # 그 이야기인 즉슨 얘가 이어져 있는 집합의 갯수를 알고 싶은 것임
    # 그것을 위해서는 겹치지 않는 집합을 사용하여야 함
    # 여기서는 disjoint set인 union find 사용
    for i in range(n):
        a, b = input().split()
        if a not in root:
            root[a] = a
            number[a] = 1
        if b not in root:
            root[b] = b
            number[b] = 1
        # union 해주어야 함
        union(a, b)
        # a로 하든 b로 하든 결과값 동일
        res.append(number[find(b)])
    print('\n'.join(map(str, res)))
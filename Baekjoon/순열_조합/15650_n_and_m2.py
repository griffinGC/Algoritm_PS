from itertools import combinations
N, M = map(int, input().split())
c = combinations(range(1, N+1), M)
for i in c:
    print(" ".join(map(str, i)))
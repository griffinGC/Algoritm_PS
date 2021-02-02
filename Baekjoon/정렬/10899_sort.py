import sys
input = sys.stdin.readline
n = int(input())
d = [0] * 10001
for _ in range(n):
    d[int(input())] += 1
for i in range(10001):
    if d[i] != 0:
        for j in range(d[i]):
            print(i)

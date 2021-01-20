# 음수는 음수끼리 묶기
# 0, 1은 묶지 않기 => 0 은 마이너스에 넣고 1은 더하기
# 2개씩 묶기
import heapq
import sys
input = sys.stdin.readline
n = int(input())
p = list()
m = list()
total = 0
for _ in range(n):
    a = int(input())
    if a <= 0:
        heapq.heappush(m, a)
    elif a > 1:
        heapq.heappush(p, -a)
    elif a == 1:
        total += 1
while True:
    if len(p) >= 2:
        cal = 1
        for _ in range(2):
            v = heapq.heappop(p)
            cal *= v
        total += cal
    else:
        break
while True:
    if len(m) >= 2:
        cal = 1
        for _ in range(2):
            v = heapq.heappop(m)
            cal *= v
        total += cal
    else:
        break
if m:
    total += heapq.heappop(m)
if p:
    total += -heapq.heappop(p)
print(total)
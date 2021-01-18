import sys
input = sys.stdin.readline
n = int(input().strip())
score = []
for _ in range(n):
    score.append(int(input().strip()))
# 등수 정렬
score.sort()
cnt = 0
# 정렬된 것을 거꾸로 차이만큼 빼오기
for i in range(n, 0, -1):
    if i != score[i-1]:
        cnt += abs(score[i-1] - i)
print(cnt)
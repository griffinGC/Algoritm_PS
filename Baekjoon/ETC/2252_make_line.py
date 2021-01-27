# 위상정렬 알고리즘 Topology Sort
import sys
from collections import defaultdict, deque
input = sys.stdin.readline
n, m = map(int, input().split())
# 앞에 있는 것이 뒤에있는 원소보다 먼저 서야함
# 선수과목이라고 생각

# 초기화 시켜줌
stu = defaultdict(list)
indegree = [0] * (n + 1)
indegree[0] = 100000
for _ in range(m):
    a, b = map(int, input().split())
    stu[a].append(b)
    indegree[b] += 1
# indegree가 가장 작은 원소 찾아냄 0 이어야만 함 => 반드시 1개일 필요는 없음
q = deque()
for i in range(n + 1):
    if indegree[i] == 0:
        q.append(i)

result = []
while q:
    now = q.popleft()
    result.append(now)
    for e in stu[now]:
        # 들어오는 숫자 삭제
        indegree[e] -= 1
        if indegree[e] == 0:
            q.append(e)

for r in result:
    print(r, end=" ")




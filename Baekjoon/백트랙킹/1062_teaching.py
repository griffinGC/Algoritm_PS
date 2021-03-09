import sys
input = sys.stdin.readline
# 780ms => 560ms
# anta, tica를 제외하고 k개의 글자
n, k = map(int, input().split())
words = []
if k < 5:
    print(0)
    exit(0)
elif k == 26:
    print(n)
    exit(0)
for _ in range(n):
    w = input()
    w = w[4:-4]
    # 넣을때 각 원소를 아스키 코드의 배열로 넣기
    t = []
    # 아스키 코드로 변경해서 그 값을 넣어버림
    for i in w:
        t.append(ord(i) - ord('a'))
    words.append(t)
alpabets = [0] * 26
init = ['a', 'n', 't', 'i', 'c']
for i in init:
    # 기본으로 들어가야 하는 애들 넣어줌
    alpabets[ord(i) - ord("a")] += 1

# 26개의 알파벳 중에서 a, n, t, i, c 제외한 애들을 조합으로 만들기
# 가능한 스펠링의 갯수
result = 0
def backtracking(index, cnt):
    global result
    # k-5인 이유는 5개인 a, n, t, i, c 는 이미 들어가있기 때문
    if cnt == k - 5:
        word_cnt = 0
        flag = True
        # 단어들을 돌면서 확인
        for wo in words:
            for ww in wo:
                if alpabets[ww] == 0:
                   flag = False
                   break
            if flag is True:
                word_cnt += 1
            flag = True
        result = max(result, word_cnt)
        return
    for i in range(index, 26):
        # 0일때만 들어가기 때문에 미리 초기화 시켜놓은 init은 상관 없음 항상 들어가있는 상태
        if alpabets[i] == 0:
            # 새로 들어가는 부분을 넣고 빼고 함으로써 조합을 계산
            alpabets[i] += 1
            # 백트래킹으로 조합 // dfs이기도 함
            backtracking(i , cnt + 1)
            alpabets[i] -= 1

backtracking(0, 0)
print(result)
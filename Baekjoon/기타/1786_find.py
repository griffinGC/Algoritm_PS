# https://bowbowbow.tistory.com/6
import sys
input = sys.stdin.readline
t = input().strip()
p = input().strip()
# 처음 인덱스가 0부터 시작!
def make_pi(words):
    # 첫번째는 무조건 0이 될 수 밖에 없음
    result = [0] * len(words)
    j = 0
    for i in range(1, len(words)):
        while j > 0 and words[i] != words[j]:
            j = result[j - 1]
        if words[i] == words[j]:
            j += 1
            result[i] = j
    return result

def kmp(stn, cmp):
    result = []
    pi = make_pi(cmp)
    j = 0
    for i in range(len(stn)):
        # 중간 단계를 넘는 부분
        while j > 0 and stn[i] != cmp[j]:
            j = pi[j - 1]
        if stn[i] == cmp[j]:
            if j == len(cmp) - 1:
                result.append(i - len(cmp) + 1)
                j = pi[j]
            else:
                j += 1
    print(len(result))
    for i in result:
        print(i + 1)
kmp(t, p)

#########################################################################

# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
def preprocessing():
    i = 1
    j = 0
    while i < m:
        if p[i] == p[j]:
            j += 1
            pi[i] = j
            i += 1
        else:
            if j != 0:
                j = pi[j-1]
            else:
                pi[j] = 0
                i += 1
# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
def kmp():
    i = 0
    j = 0
    while i < n:
        if p[j] == t[i]:
            i += 1
            j += 1
        # 같을 경우 i, j를 추가하고 바로 다음 위치를 현재 한번 더 확인
        if j == m:
            result.append(i-j+1)
            j = pi[j-1]
        elif i < n and p[j] != t[i]:
            # pi[j-1]로 보는 것이 아니라 j로 확인하네..
            # j != 0 이라는 것은 어떤 중간 지점을 보고 있다라는 것이므로 매치되는 부분을 찾는것
            # 이 과정에서 처음부터 다시 조회할 수도 있고 아니ㄹ 수도 있음
            if j != 0:
                j = pi[j-1]
            # j == 0 이라는 것은 첫지점을 비교중이었다는 것이므로 그냥 i를 증가해서 첫지점 비교
            else:
                i += 1
t = input()
p = input()
n, m = len(t), len(p)
pi = [0] * m
result = []
preprocessing()
kmp()
print(len(result))
print(' '.join(map(str, result)))

################################################################################################

t = input()
p = input()
def make_pi(words):
    result = [0] * len(words)
    j = 0
    for i in range(1, len(words)):
        while j > 0 and words[i] != words[j]:
            j = result[j - 1]
        if words[i] == words[j]:
            j += 1
            result[i] = j
    return result

def kmp(stn, cmp):
    pi = make_pi(cmp)
    i, j = 0, 0
    matched = 0
    result = []
    # 계속해서 일정 갯수가 되는지 카운트 하는것이기 때문에 일정갯수만큼 확인
    # 고로 실패가 뜸
    # 같지 않을 경우 j = 0으로 계속 초기화를 시키는 것이 아닌 현재까지 같았던 부분을 다시 넣어서 kmp 수행
    while (i + len(cmp)) <= len(stn):
        if matched < len(cmp) and stn[i + matched] == cmp[matched]:
            matched += 1
            if matched == len(cmp):
                result.append(i - j + 1)
        else:
            if matched == 0:
                i += 1
            else:
                i += matched - pi[matched - 1]
                matched = pi[matched - 1]
    print(len(result))
    for i in result:
        print(i, end=" ")
kmp(t, p)
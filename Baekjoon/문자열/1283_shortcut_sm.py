import sys
input = sys.stdin.readline
n = int(input())

def solution():
    alpha = [0] * 26 # 알파벳 사용 여부
    idx = -1 # 단축키가 설정될 인덱스
    ans = [''] * n # 정답
    for k in range(n):
        word = input().strip() # 인덱싱을 위한 word
        wordArr = word.split() # 각 단어의 첫번째 알파벳 확인하기 위한 word배열
        check = [0, 0] # [단어의 첫번째 알파벳에서 발견, 단어의 두번째 알파벳 이상에서 발견]
        l = 0 # wordArr에서 단어의 길이를 누적으로 더하는 변수
        # 단어의 첫번째 음절에서 발견될 때
        for j in range(len(wordArr)):
            tmp = wordArr[j][0].lower()
            if not alpha[ord(tmp) - ord('a')]:
                alpha[ord(tmp) - ord('a')] = 1
                idx = l
                check[0] = 1
                break
            l += len(wordArr[j]) + 1
        l = 0
        # 단어의 두번째 음절이상에서 발견될 때
        if not check[0]:
            for i in range(len(wordArr)):
                # 이미 발견 됐을 때
                if check[1]:
                    break
                for j in range(1, len(wordArr[i])):
                    tmp = wordArr[i][j].lower()
                    if not alpha[ord(tmp) - ord('a')]:
                        alpha[ord(tmp) - ord('a')] = 1
                        idx = l + j
                        check[1] = 1
                        break
                l += len(wordArr[i]) + 1
        # 첫번째나 두번째 이상의 음절에서 단축키를 설정할 수 있는 경우
        if check[0] or check[1]:
            ans[k] = word[:idx] + '[' + word[idx] + ']' + word[idx + 1:]
        # 단축키를 설정할 수 없는 경우
        else:
            ans[k] = word
    print("\n".join(map(str, ans)))
solution()
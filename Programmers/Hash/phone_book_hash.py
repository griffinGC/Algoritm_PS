# 어떤 번호가 다른 번호의 접두어인 경우 false
import collections
def solution(phone_book):
    answer = True
    dict_list = dict(collections.Counter(phone_book))
    # 시간 복잡도 해결 필요
    for ele in phone_book:
        for a in phone_book:
            if ele in a[0:len(ele)]:
                dict_list[ele] += 1
                if dict_list[ele] > 2:
                    answer = False
    return answer

# 효율성 처리
def solution2(phone_book):
    phone_book.sort()
    answer = True
    dict_list = dict(collections.Counter(phone_book))
    print(phone_book)
    for index in range(len(phone_book)-1):
        # 정렬을 하면 같은게 겹치는 순서대로 정렬되기 때문
        # 데이터의 크기를 뜻하는 것이 아님 11 88 113 있으면 11 113 88
        if phone_book[index] in phone_book[index+1]:
            answer = False
    return answer
pb = ["119", "97674223", "1195524421"]
pb2 = ["123","456","789"]
pb3 = ["88","123","1235","567","12"]
result1 = solution(pb)
print(result1)
result2 = solution(pb2)
print(result2)
result3 = solution(pb3)
print(result3)
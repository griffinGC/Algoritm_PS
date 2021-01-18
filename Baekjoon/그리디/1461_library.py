import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
book_list = list(map(int, input().split()))
def solution(books):
    minus, plus = list(), list()
    books.sort()
    for b in books:
        if b < 0:
            heapq.heappush(minus, b)
        else:
            heapq.heappush(plus, -b)
    max_val = max(max(books), -min(books))
    total = 0
    while minus:
        val1 = -heapq.heappop(minus)
        for i in range(m - 1):
            if minus:
                -heapq.heappop(minus)
            else:
                break
        total += val1 * 2
    while plus:
        val2 = -heapq.heappop(plus)
        for j in range(m - 1):
            if plus:
                -heapq.heappop(plus)
            else:
                break
        total += val2 * 2
    total -= max_val
    return total
result = solution(book_list)
print(result)
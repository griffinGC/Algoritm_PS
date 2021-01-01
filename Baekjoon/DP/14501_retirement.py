import sys
input = sys.stdin.readline

data = list()
# data.append((0,0))
n = int(input())
for _ in range(n):
    a,b = map(int, input().split())
    data.append((a,b))

def solution(n, data):
    len_data = len(data)
    tabulate_table = [[0 for i in range(n + 1)] for j in range(len_data + 1)]
    for i in range(len_data + 1):
        for w in range(n + 1):
            # print("data[i][0], ", data[i][0])
            # print("w", w)
            if i == 0 or w == 0:
                tabulate_table[i][w] = 0
            elif data[i-1][0] <= w:
                tabulate_table[i][w] = max(data[i-1][1] + tabulate_table[i-1][w - data[i-1][0]], tabulate_table[i-1][w])
            else:
                tabulate_table[i][w] = tabulate_table[i][w]
    return tabulate_table[len_data][n]

print(data)
result = solution(n, data)

print(result)
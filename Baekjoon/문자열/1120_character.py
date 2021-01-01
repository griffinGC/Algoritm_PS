def solution():
    a, b = input().split()
    diff_num = len(b) - len(a)
    result = len(b)
    for i in range(diff_num + 1):
        count = 0
        for j in range(len(a)):
            if a[j] != b[i + j]:
                count += 1
        result = min(result, count)

    return result
result = solution()
print(result)
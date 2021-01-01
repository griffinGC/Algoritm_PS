def solution2():
    num = int(input())
    weight_list = list(map(int, input().split()))
    result = list()
    for i in weight_list:
        if len(result) == 0:
            result.append(i)
            continue
        if i > result[-1]:
            result.append(i)
        else:
            index = bisect.bisect_left(result, i)
            result[index] = i
    return len(result)
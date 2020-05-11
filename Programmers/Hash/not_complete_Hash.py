def solution(participant, completion):
    answer = ""
    dic_list = {}
    for e in participant:
        if dic_list.get(e) != None and dic_list[e] > 0:
            dic_list[e] += 1
        dic_list[e] = dic_list.get(e,1)
    for e in completion:
        dic_list[e] -= 1
    for keys in dic_list.keys():
        if dic_list[keys] > 0:
            return keys
    return answer

part = ["leo", "kiki", "eden"]
com = ["eden", "kiki"]
result = solution(part, com)
print(result)

part2 = ["mislav", "stanko", "mislav", "ana"]
com2 = ["stanko", "ana", "mislav"]
result2 = solution(part2, com2)
print(result2)
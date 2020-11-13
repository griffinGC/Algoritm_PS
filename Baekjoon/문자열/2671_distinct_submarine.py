import re
sound = input()
def solution(sound):
    try:
        regx = re.compile('(100+1+|01)+')
        result = regx.fullmatch(sound)
        s, e = result.start(), result.end()
        return "SUBMARINE"
    except:
        return "NOISE"

result = solution(sound)
print(result)



tc1 = "100101100000000001101"
tc2 = "100000000001101100000000001101"
tc3 = "101"
result = solution(tc1)
print(result)
result2 = solution(tc2)
print(result2)
result3 = solution(tc3)
print(result3)
import sys
input = sys.stdin.readline
n = int(input())
liquid_list = list(map(int, input().split()))
st, end = 0, n - 1
tmp1, tmp2 = st, end
# abs 적게 사용해서 시간 극대화
close = abs(liquid_list[st] + liquid_list[end])
while st < end:
    val = liquid_list[st] + liquid_list[end]
    val_temp = abs(val)
    if val == 0:
        tmp1, tmp2 = st, end
        break
    if val_temp < close:
        close = val_temp
        tmp1, tmp2 = st, end
    if val < 0:
        st += 1
    if val > 0:
        end -= 1

print(liquid_list[tmp1], liquid_list[tmp2])
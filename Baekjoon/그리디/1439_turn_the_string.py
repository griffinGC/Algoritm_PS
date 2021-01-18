# 변경되는 순간을 각 리스트에 넣어주고 리스트의 갯수중 작은 것을 리턴
number = input()
f, s = list(), list()
init = number[0]
if init == '0':
    f.append(0)
else:
    s.append(0)
for i in range(len(number)):
    if number[i] != init:
        if number[i] == '0':
            f.append(i)
        else:
            s.append(i)
        init = number[i]
print(min(len(f), len(s)))
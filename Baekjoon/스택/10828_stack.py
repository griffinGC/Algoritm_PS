import sys
input = sys.stdin.readline
o = int(input())
data = []
for i in range(o):
    op = input().split()
    if op[0] == "push":
        data.append(int(op[1]))
    elif op[0] == "pop":
        if data:
            print(data.pop())
        else:
            print(-1)
    elif op[0] == "size":
        print(len(data))
    elif op[0] == "empty":
        if data:
            print(0)
        else:
            print(1)
    elif op[0] == "top":
        if data:
            print(data[-1])
        else:
            print(-1)

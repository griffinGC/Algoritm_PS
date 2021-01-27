from collections import deque
import sys
input = sys.stdin.readline
o = int(input())
d = deque()
for _ in range(o):
    op = input().split()
    if op[0] == "push_front":
        d.appendleft(int(op[1]))
    elif op[0] == "push_back":
        d.append(int(op[1]))
    elif op[0] == "pop_front":
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif op[0] == "pop_back":
        if d:
            print(d.pop())
        else:
            print(-1)
    elif op[0] == "size":
        print(len(d))
    elif op[0] == "empty":
        if d:
            print(0)
        else:
            print(1)
    elif op[0] == "front":
        if d:
            print(d[0])
        else:
            print(-1)
    elif op[0] == "back":
        if d:
            print(d[-1])
        else:
            print(-1)
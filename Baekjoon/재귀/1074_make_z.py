def solve(len, x, y):
    global result

    if X < x + len and X >= x and Y < y + len and Y >= y:
        if len == 2:
            if x == X and y == Y:
                print(int(result))
                return
            result += 1
            if x == X and y + 1 == Y:
                print(int(result))
                return
            result += 1
            if x + 1 == X and y == Y:
                print(int(result))
                return
            result += 1
            if x + 1 == X and y + 1 == Y:
                print(int(result))
                return
            result += 1
            return
        solve(len / 2, x , y)
        solve(len / 2, x, y + len / 2)
        solve(len / 2, x + len / 2, y)
        solve(len / 2, x + len / 2, y + len / 2)
    else:
        result += len*len

# 속도 더 빠름
def solve2(len, x, y):
    global result
    if x == X and y == Y:
        print(int(result))
        return
    if X < x + len and X >= x and Y < y + len and Y >= y:
        solve(len / 2, x , y)
        solve(len / 2, x, y + len / 2)
        solve(len / 2, x + len / 2, y)
        solve(len / 2, x + len / 2, y + len / 2)
    else:
        result += len*len

result = 0
N, X, Y = map(int, input().split())
solve(2**N, 0, 0)
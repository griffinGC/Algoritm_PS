import math
# 안에 있다면 True 리턴
# 안에 없다면 False 리턴
def check(x, y, dx, dy, rr):
    nx = abs(x - dx)
    ny = abs(y - dy)
    if rr - math.sqrt(((nx * nx) + (ny * ny))) > 0:
        return True
    else:
        return False

t = int(input())
        
for _ in range(t):
    sx, sy, ex, ey = map(int, input().split())
    n = int(input())
    circles = list()
    # 반지름이 가장 작은것부터 오름차순으로 정렬
    for _ in range(n):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    circles.sort(key=lambda x: x[2])
    f_in = False
    in_check = 0
    
    for a, b, c in circles:
        start_check = check(sx, sy, a, b, c)
        end_check = check(ex, ey, a, b, c)
        if start_check is True and end_check is True:
            continue
        elif start_check is True or end_check is True:
            in_check += 1
    # print("answer")
    print(in_check)
    
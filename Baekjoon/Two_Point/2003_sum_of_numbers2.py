n, m = map(int, input().split())
list = list(map(int,list(input().split())))

sum, end, count = 0,0,0

for start in range(n):
    while sum < m and end < n:
        sum += list[end]
        end += 1

    if sum == m:
        count += 1

    sum -= list[start]

print(count)
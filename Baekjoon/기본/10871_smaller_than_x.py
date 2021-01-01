n, x = map(int, input().split())
num_list = list(map(int, input().split()))
for n in num_list:
    if n < x:
        print(n, end=" ")
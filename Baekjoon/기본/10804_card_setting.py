num_list = [i+1 for i in range(20)]
for _ in range(10):
    st, end = map(int, input().split())
    t = num_list[st-1:end]
    num_list[st-1:end] = reversed(t)
for i in num_list:
    print(i, end=" ")
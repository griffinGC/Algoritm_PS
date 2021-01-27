import bisect
n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
ms = list(map(int, input().split()))
for d in ms:
    index = bisect.bisect_left(a, d)
    if index >= n or a[index] != d:
        print("0")
    elif a[index] == d:
        print("1")
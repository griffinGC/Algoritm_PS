import sys
input = sys.stdin.readline
i = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0:
        exit(0)
    cnt = 0
    mod = v // p
    div = l if v % p >= l else v % p
    cnt += mod * l + div
    print("Case {0}: {1}".format(i, cnt))
    i += 1
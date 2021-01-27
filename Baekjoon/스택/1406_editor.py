import sys
input = sys.stdin.readline
st1 = list(input().strip())
st2 = []
n = int(input())
for _ in range(n):
    s = input().split()
    if s[0] == "L":
        if st1:
            st2.append(st1.pop())
    elif s[0] == "D":
        if st2:
            st1.append(st2.pop())
    elif s[0] == "B":
        if st1:
            st1.pop()
    elif s[0] == "P":
        st1.append(s[1])
print("".join(st1 + st2[::-1]))

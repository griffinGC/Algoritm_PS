a = int(input())
first, second = 0, 1
while a > 0:
    first, second = second, first + second
    a -= 1

print(first)
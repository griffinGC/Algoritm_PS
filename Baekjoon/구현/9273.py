while True:
    cal_num = ""
    try:
        cal_num = int(input()[2:])
    except EOFError:
        exit(0)
    answer = 0
    for i in range(cal_num + 1, 2 * cal_num + 1):
        answer = answer + 1 if i * cal_num % (i - cal_num) == 0 else answer
    print(answer)

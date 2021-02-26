n = int(input())
words = [input() for _ in range(n)]
shortcut = set()
def check_shortcut(word):
    global shortcut
    for i in range(len(word)):
        if word[i].upper() not in shortcut and word[i] != " ":
            shortcut.add(word[i].upper())
            return word[:i] + "[" + word[i] + "]" + word[i + 1:]
    return ""
for w in words:
    w_list = w.split()
    # flag
    flag = False
    for k in range(len(w_list)):
        ws = w_list[k]
        if ws[0].upper() not in shortcut:
            for i in range(len(ws)):
                if ws[i].upper() not in shortcut and ws[i] != " ":
                    shortcut.add(ws[i].upper())
                    flag = True
                    p = ws[:i] + "[" + ws[i] + "]" + ws[i + 1:]
                    w_list[k] = p
                    print(" ".join(w_list))
                    break
        if flag is True:
            break
        else:
            continue
    if flag is False:
        p = check_shortcut(w)
        if len(p) != 0:
            print(p)
            flag = True
    if flag is False:
        print(w)
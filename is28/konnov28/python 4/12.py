
def clean_spaces(s):
    res = ''
    prev = True
    for i in range(len(s)):
        if s[i] == ' ':
            if prev:
                continue
            else:
                prev = True
                res += s[i]
        else:
            prev = False
            res += s[i]
    return res

s = "    Сколько   же  здесь        пробелов ...   а последний   останется    "
print("Было:", s)
print("Стало:", clean_spaces(s))

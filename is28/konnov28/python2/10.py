
def reverse(s):
    res = ''
    for i in range(len(s) - 1, -1, -1):
        res += s[i]
    return res

s = "а роза упала на лапу Азора"
print("Было:", s)
print("Стало:", reverse(s))

s = "лилипут сома на мосту пилил"
print("Было:", s)
print("Стало:", reverse(s))


def find(s, sub):
    res = False
    for i in range(len(s)):
        found = True
        for j in range(len(sub)):
            if s[i + j] != sub[j]:
                found = False
                break
        if found:
            res = True
            break
    return res

s = "Питон велик! Питон могуч!"

sub = "могуч"
r = find(s, sub)
print("В строке '", s, "'", "встречается" if r else "не встречается", "подстрока '", sub, "'")

sub = "слаб"
r = find(s, sub)
print("В строке '", s, "'", "встречается" if r else "не встречается", "подстрока '", sub, "'")

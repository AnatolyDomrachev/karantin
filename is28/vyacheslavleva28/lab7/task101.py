def func(a):
    size = len(a)
    r=""
    for i in range(size):
        r += a[size-1-i]
    return r

		


strc = input()
res_str = func(strc)
print(res_str)

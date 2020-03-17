
def func(str1, str2, num):
    a = ""
    for i in range(num):
        a += str1[i]
    a += str2

    for i in range(num, len(str1)):
        a += str1[i]

    return a

str1 = input()
str2 = input()
num = int(input())
res_str=func(str1, str2, num)
print(res_str)

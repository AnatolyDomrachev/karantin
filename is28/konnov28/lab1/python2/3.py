from array import array


def count(items, x):
    res = 0
    for i in range(len(items)):
        if items[i] == x:
            res += 1
    return res


l = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
arr = array("i", l)
x = 3

r = count(l, x)
print("Элемент", x, "встречается в ЛИСТЕ столько раз:", r)

r = count(arr, x)
print("Элемент", x, "встречается в МАССИВЕ столько раз:", r)

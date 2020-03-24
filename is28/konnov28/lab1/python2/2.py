from array import array


def find_last_position(items, x):
    pos = -1
    for i in range(len(items) - 1, -1, -1):
        if items[i] == x:
            pos = i
            break
    return pos


l = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
arr = array("i", l)
x = 3

p = find_last_position(l, x)
print("Последний раз элемент", x, "встречается в ЛИСТЕ на позиции", p)

p = find_last_position(arr, x)
print("Последний раз элемент", x, "встречается в МАССИВЕ на позиции", p)


def vvod(s, d, i):
 return d[:i] + s + d[i:]


s=input("Введите добавляемое число:")
d="123456789"
i=int(input("Введите позицию  в которóю добавится число:"))
print(vvod(s,d,i))

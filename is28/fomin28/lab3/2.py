x=int(input("введите трехзначное число"))
i= x % 10
y= (x//10) % 10
z= (x//100) % 10
sum= i+y+z
print(sum)

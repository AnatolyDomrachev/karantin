# произведения по строкам
for i in range(0,10):
    for j in range(0,10):
        print(i, "*", j, "=", i * j)


# в табличной форме:
print("\t", end="")
for i in range(0,10):
    print(i, end="\t")
print("")

for i in range(0,10):
    print(i, end="\t")
    for j in range(0,10):
        print(i * j, end="\t")
    print("")

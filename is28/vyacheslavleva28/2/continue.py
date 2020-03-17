for x in range(-1000,1001):
    for y in range(-1000,1001):
        if x*y < 0:
            continue
        if -y**2 + x**4 == 0 and -2*y**2 + 2*x**4 == 0:
            print(x,y)
print("END")


ok = 0
for x in range(-1000,1001):
    if ok == 5:
        break
    for y in range(-1000,1001):
        if ok == 5:
            break
        if x*y > 0:
            if -y**2 + x**4 == 0 and -2*y**2 + 2*x**4 == 0:
                print(x,y)
                ok+=1
print("END")


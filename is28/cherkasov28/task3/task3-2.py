def dataInput():
    print("Введите массив x:")
    x = list(map(float,input("").split()))

    print("\nВведите массив y:")
    y = list(map(float,input("").split()))

    print("\nВведите массив z:")
    z = list(map(float,input("").split()))
    return x,y,z

def findArrayWithMinimalElement(x,y,z):
    minElement = min( [min(x),min(y),min(z)] )
    print(x if minElement == min(x) else (y if minElement == min(y) else z ))

x,y,z = dataInput()
findArrayWithMinimalElement(x,y,z)
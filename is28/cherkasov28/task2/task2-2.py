def findArrayWithMinimalElement(x,y,z):
    minElement = min( [min(x),min(y),min(z)] )
    print(x if minElement == min(x) else (y if minElement == min(y) else z ))


x = [0,1,2,3,4]
y = [5,-3.5,0.42,9.32,15]
z = [-0.43,8.22,-9.14,2,6.5]

print("Массив с наименьшим элементом: ",)
findArrayWithMinimalElement(x,y,z)
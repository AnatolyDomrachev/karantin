def vvod_str():
    a=str(input('Введите строкó:'))
    return a
    
def kolichestvo_simvolov(str1, str2):
    a=len(str1)
    b=len(str2)
    return a,b
    
def rashet(str1, str2):
    x=[]
    a,b = kolichestvo_simvolov(str1, str2)
    for i in range(a):
      if str1[i] in str2:
         x.append(str1[i])
    return x

    
    



str1=vvod_str()
str2=vvod_str()
massiv=rashet(str1, str2)
print(massiv)




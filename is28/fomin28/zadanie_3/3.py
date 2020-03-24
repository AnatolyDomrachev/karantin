def vvod_dannyh():
 for i in range(0,10):
   a[i]=int(input("введите число массива"))  
 return(a)

def raschet():
 b=0
 for i in range(0,10):
   	if a[i] == x:
      		b=1
      		break
 return(b)

def vyvod_dannyh(): 
 if b==1:
    print("число ",x," eсть в массиве")
 else:
    print("такого числа нет в массиве")

a = [0,0,0,0,0,0,0,0,0,0]

x=0

a = vvod_dannyh()

x=int(input("введите искомое число"))   

b=raschet()
print(vyvod_dannyh())

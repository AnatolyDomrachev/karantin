def vvod_dannyh():
 f = open('data.txt', 'r')
 for i in range(0,10):
   a[i]=int(f.readline())  
 return(a)

def raschet():
 b=0
 for i in range(0,10):
   	if a[i] == x:
      		b=1
      		break
 return(b)

def vyvod_dannyh():
 f = open('res.txt', 'w') 
 if b==1:
    print("число ",x," eсть в массиве", file = f )
 else:
    print("такого числа нет в массиве",file = f)
 return()

a = [0,0,0,0,0,0,0,0,0,0]

x=0

a = vvod_dannyh()

x=int(input("введите искомое число"))   

b=raschet()
vyvod_dannyh()

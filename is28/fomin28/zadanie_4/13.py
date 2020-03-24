def dlinna_slova():
 stroka=str(input('vvod stroki: '))
 a=[]
 x=int(0)
 a=stroka.split(' ')


 for i in range(len(a)):
    y=int(len(a[i]))
    if y>x:
      x = len(a[i])
 
 return(x)
print(dlinna_slova())

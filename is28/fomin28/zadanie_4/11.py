def funct11():
 a=str(input('enter 1st string '))
 b=str(input('enter 2nd string '))
 arr=[]
 lena=len(a)
 lenb=len(b)
 arrlen=len(arr)
 
 for i in range(lena):
    for n in range(lenb):
       if a[i]==b[n]:
         arr.append(a[i])
         break

        

 return(arr)
arr=funct11()
print(arr)


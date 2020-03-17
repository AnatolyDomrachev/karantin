def masslov():
 arr=[]
 kostil=str('placeholder')
 slov={}
 x=str(input('enter file name: '))
 f=open(x,'r')
 m=0
 slov2={}
 
 while kostil != '':
     kostil=(f.readline().replace('\n', ''))
     m=kostil.split(':')
     if kostil != '':
      	slov={'name':m[0],'age':m[1]}
      	arr.append(slov)
    
 slov2={'name':str(input('enter name ')),'age':str(input('enter age '))}
 arr.append(slov2)
 f.close
 f=open(x,'w')
 for i in arr:
    print(i['name'],':',i['age'],file=f)
 
 print(arr)

 
 return(arr)
masslov()


def masslov():
 arr=[]
 kostil=str('placeholder')
 slov={}
 f=open('data','r')
 m=0
 s=str(input('enter str: '))
 
 while kostil != '':
     kostil=(f.readline().replace('\n', ''))
     m=kostil.split(':')
     if kostil != '':
      	slov={'name':m[0],'age':m[1]}
      	arr.append(slov)
 
 if s == '':
   print(arr)
 for i in range(3):
    if arr[i]['name']==s or arr[i]['age']==s:
       print(arr[i])

 
 return(arr)
masslov()

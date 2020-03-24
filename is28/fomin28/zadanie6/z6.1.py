def masslov():
 arr=[]
 kostil=str('placeholder')
 slov={}
 f=open('data','r')
 m=0
 
 
 while kostil != '':
     kostil=(f.readline().replace('\n', ''))
     m=kostil.split(':')
     if kostil != '':
      	slov={'name':m[0],'age':m[1]}
      	arr.append(slov)
 
 
 print(arr)

 
 return(arr)
masslov()

 

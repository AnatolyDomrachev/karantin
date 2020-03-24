a=[]
v = {}
for i in range(2):
    v['name'] = input('name: ')
    v['age'] = input('age: ') 
    v['grp'] = input('grp: ') 
    a.append(v.copy())

print(a)
print("name \t age \t grp")
for x in a:
    print(x['name']+" \t "+x['age']+" \t "+x['grp'])



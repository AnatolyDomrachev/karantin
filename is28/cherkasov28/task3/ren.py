import os

for i in range(1,3):
    pathway = "lab6-"+str(i)+".py"
    newPathWay = "task3-"+str(i)+".py"
    with open(pathway) as file:
        contents = file.read()
    os.remove(pathway)
    with open(newPathWay,'w') as file:
        file.write(contents)
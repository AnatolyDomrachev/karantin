def func():
    a=[]
    n=int(input())
    for i in range(n):
        a.append(int(input()))
    print("4islo x")
    x=int(input())
    for i in range(len(a)):
        if a[i]==x:
            print(i)
            quit()
    print(False)

func()    
        

def func(a, d):
    b=a.split()
    c=0
    for i in range(len(b)):
        if b[i]==d:
            c=c+1
    print(c)
    
    
string=input()
word=input()
func(string, word)

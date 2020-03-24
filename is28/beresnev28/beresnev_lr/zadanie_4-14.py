b=[]

def dis_str(sr):
    k=0
    sr=sr+" "
    sr=list(sr)
    for a in range(len(sr)):
        k=k+1
        if sr[a] == " ":
                    b.append(k-1)
                    k=0
    return(b)

sr=str(input("input str - "))
l=dis_str(sr)
print(l)
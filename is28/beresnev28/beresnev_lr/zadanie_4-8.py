
def input_d():
	s1=str(input('1 = '))
	s2=str(input('2 = '))
	n=int(input("n = "))
	return(s1,s2,n)

def paste_def(s1,s2,n):
	sr=list(s2)
	t=sr[n-1]
	s2=s2.replace(t,s1)
	return(s2)

s1,s2,n=input_d()
s2=paste_def(s1,s2,n)
print(s2)
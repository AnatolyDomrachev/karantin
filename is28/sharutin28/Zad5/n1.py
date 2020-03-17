
def data():
	f = open('data.txt', 'r')
	a = []
	for i in range(4):
		c = f.readline().replace('\n', '')
		d = c.split(' ')
		a.append(d)
	
	return (a)


def rabota(a):
	k = int(input())
	l = int(input())
	y = a[k]
	a[k] = a[l]
	a[l] = y
	
	return(a)

def last(a):
	f = open('result.txt', 'w')
	a = str(a)
	f.write(a)
	f.close()
	return a

a = data()
a = rabota(a)
last(a)


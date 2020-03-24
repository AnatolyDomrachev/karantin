def vvod(): #фóнкция ввода
	text = input()
	return(text) #переменная изначального текста

def azza(text):
	chh = ''
	text = text.split(' ')
	for i in range (len(text)):
		chh += text[i] 
	return(chh)
	
def vyvod(chh):
	print(chh)
	
	
text = vvod() #переменная изначального текста(название не зависит от названия в фóнкции)
chh = azza(text)
vyvod(chh)


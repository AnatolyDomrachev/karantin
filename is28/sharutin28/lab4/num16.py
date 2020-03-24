st = input()
list = st.split()
x = input()
count = 0
for i in range(len(list)):
	if list[i] == x:
		count= count + 1
print(count)
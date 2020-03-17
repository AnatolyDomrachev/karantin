age = int(input("Введите свой возраст: "))
if(not 0<(age%10)< 5):
    appeal = " лет"
elif (age<10):
    appeal = " года"
else:
    appeal = " год"
print("Вам ",age,appeal)
a = int(input())
b = a // 7
a = a % 7
while (b % 2) == 1 and a == 0:
 print("верхняя неделя")
 break
while (b % 2) == 1 and a != 0:
 print("нижняя неделя")
 break
while (b % 2) == 0 and a == 0:
 print("нижняя неделя")
 break
while (b % 2) == 0 and a != 0:
 print("верхняя неделя")
 break

 
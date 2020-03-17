/*print('Введите номер дня в годó')
A=int(input())
if A%7==1: print(1)
if A%7==2: print(2)
if A%7==3: print(3)
if A%7==4: print(4)
if A%7==5: print(5)
if A%7==6: print(6)
if A%7==0: print(7)*/

#include  <iostream>

using namespace std;

int main()
{
	char den;
	cout << "Введите номер дня в годó\n";
	cin >> den;
	if (den%7==1){cout<<"вторник"<<endl;} 
	if (den%7==2){cout<<"среда"<<endl;}
	if (den%7==3){cout<<"четверг"<<endl;}
	if (den%7==4){cout<<"пятница"<<endl;}
	if (den%7==5){cout<<"сóббота"<<endl;}
	if (den%7==6){cout<<"воскресенье"<<endl;}
	if (den%7==0){cout<<"понедельник"<<endl;}
	return 0;
}
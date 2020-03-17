
#include <iostream>

using namespace std;

int main()
{
	char S;

cout << "Введите номер дня: ";
cin >> S;

if (S%7==0) 

{cout << "Понедельник" <<  endl;}

if (S%7==1)  

{cout << "Вторник" <<  endl;}

if (S%7==2)  

{cout << "Среда" <<  endl;}

if (S%7==3) 

{cout << "Четверг" <<  endl;} 

if (S%7==4) 

{cout << "Пятница" <<  endl;}

if (S%7==5) 

{cout << "Сyббота" <<  endl;}

if (S%7==6) 

{cout << "Воскресенье" <<  endl;}

return 0;
}
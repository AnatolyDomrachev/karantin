#include <string>
#include <iostream>
#include<cmath>
using namespace std;
struct name_age
{
	int chislo;
	
};

int main()
{
	int chislo;
	cout<<"Введите число:  "<<endl;
	cin>>chislo;
	if (chislo%7==0){cout<<"Воскресенье"<<endl;};
	if (chislo%7==1){cout<<"Понедельник"<<endl;};
	if (chislo%7==2){cout<<"Вторник"<<endl;};
	if (chislo%7==3){cout<<"Среда"<<endl;};
	if (chislo%7==4){cout<<"Четверг"<<endl;};
	if (chislo%7==5){cout<<"Пятница"<<endl;};
	if (chislo%7==6){cout<<"Сyббота"<<endl;};
}
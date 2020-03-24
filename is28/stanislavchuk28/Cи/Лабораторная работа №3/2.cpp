#include <string>
#include <iostream>
#include<cmath>
using namespace std;
struct name_age
{
	int chislo;
	int soten;
	int des;
	int edin;
	int summa;
};

int main()
{
	int chislo,soten,des,edin,summa;
	cout<<"Введите число:  "<<endl;
	cin>>chislo;
	soten = chislo/100;
	chislo= chislo%100;
	des = chislo/10;
	chislo= chislo%10;
	edin=chislo;
	summa= soten+des+edin;
	cout<<summa<<"  Сyмма цифр  "<<endl;
}
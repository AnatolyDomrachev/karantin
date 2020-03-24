#include <string>
#include <iostream>
#include<cmath>
using namespace std;
struct name_age
{
	int chislo;
	int a;
	
};

int main()
{
	int chislo,a;
	cout<<"Введите число:  "<<endl;
	cin>>chislo;
	a=bool(chislo%4);
	if (a=0) {cout<<"FALSE"<<endl;} else {cout<<"TRUE"<<endl;};
}
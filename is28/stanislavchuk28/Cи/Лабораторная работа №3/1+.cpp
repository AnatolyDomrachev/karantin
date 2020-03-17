#include <string>
#include <iostream>
#include<cmath>
using namespace std;
struct name_age
{
	double a;
	int b;
	int z;
};

int main()
{
	double a,b,z;
	cout<<"Введите число:  "<<endl;
	cin>>a;
	z=a-floor(a);
	cout<<floor(a)<<"  Целая часть   "<<z<<"      Дробная часть:"<<endl;
}
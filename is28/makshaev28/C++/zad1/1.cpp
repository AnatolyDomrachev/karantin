#include <iostream>

using namespace std;

int main()
{
	int x,y,z,Max;
	cout<<endl<<"Введите первое число: ";
	cin>>x;
	
	cout<<endl<<"Введите второе число: ";
	cin>>y;
	
	cout<<endl<<"Введите третье число: ";
	cin>>z;
	
	if (x>y){
		if(x>z) Max=x;
		else Max=z;
	}
	else {
		if(y>z)Max=y;
		else Max=z;
	}
	cout<<"Наибольшее число из введеных равно : "<<Max<<endl;
}	
